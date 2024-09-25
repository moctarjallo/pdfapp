import requests

class Media:
    def __init__(self, phone_number_id, access_token):
        self.phone_number_id = phone_number_id
        self.access_token = access_token

    def __upload(self, media_path):

        upload_url = f"https://graph.facebook.com/v20.0/{self.phone_number_id}/media"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        params = {
            "messaging_product": "whatsapp"
        }
        files = {
            'file': ('Employee_Leave_Report.pdf', open(media_path, 'rb'), 'application/pdf')
        }
        response = requests.post(upload_url, headers=headers, params=params, files=files)

        if response.status_code == 200:
            media_id = response.json().get("id")
            print(f"Media uploaded successfully, media ID: {media_id}")
        else:
            print(f"Failed to upload media: {response.status_code}")
            print(response.text)

        return media_id


    def send(self, media_path, destination_phone_number, message="Bonne reception."):

        media_id = self.__upload(media_path)

        url = f"https://graph.facebook.com/v20.0/{self.phone_number_id}/messages"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "to": f"{destination_phone_number}",
            "type": "document",
            "document": {
                "id": media_id,
                "caption": f"{message}.",
                "filename": f"{media_path.split("/")[-1].capitalize()}"
            }
        }

        response = requests.post(url, headers=headers, json=data)

        print("Media sent successfully !")

        self.__delete(media_id)

    def __delete(self, media_id):
        delete_url = f"https://graph.facebook.com/v20.0/{media_id}"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.delete(delete_url, headers=headers)

        if response.status_code == 200:
            print("Media deleted successfully!")
        else:
            print(f"Failed to delete media: {response.status_code}, {response.text}")

if __name__ == "__main__":

    Media(458857697302383, 
        "EAAMfJJStAz4BOZCknQ0VUznrDXTEKNPKwXJhnae2V1HfTv3"
        "ghtgM4NEDfQI4JuxfVDofOUeM7qojXC6NvczKlaXE6T7EY8Q"
        "YZBggn4TvWC8VxopgpFdZCc4uv8fjwUnodwSujMMEG4oZARR"
        "NW4jt0D2O0i22wotbLIq0HZCKjp7KTHqohEZBdTHm2Bavoh8"
        "vHOxtE94pSdsiG6rIuulfKmxbltfAaS"
    ).send("notification_conge.pdf", "221771332916", "Bon conges!")
