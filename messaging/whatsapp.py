import requests

class Media:
    def __init__(self, phone_number_id, access_token):
        self.phone_number_id = phone_number_id
        self.access_token = access_token


    def upload_media(self, media_path):

        # URL for media upload
        upload_url = f"https://graph.facebook.com/v20.0/{self.phone_number_id}/media"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        # Parameters including messaging_product
        params = {
            "messaging_product": "whatsapp"  # Required parameter
        }

        # Open the local PDF file with the provided path
        files = {
            'file': ('Employee_Leave_Report.pdf', open(media_path, 'rb'), 'application/pdf')
        }

        # Make a POST request to upload the file
        response = requests.post(upload_url, headers=headers, params=params, files=files)

        # Check if the upload was successful
        if response.status_code == 200:
            media_id = response.json().get("id")
            print(f"Media uploaded successfully, media ID: {media_id}")
        else:
            print(f"Failed to upload media: {response.status_code}")
            print(response.text)

        return media_id


    def send_media(self, media_id, file_name, destination_phone_number):
        # Now, send the document using the media_id
        url = "https://graph.facebook.com/v20.0/458857697302383/messages"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "to": f"{destination_phone_number}",
            "type": "document",
            "document": {
                "id": media_id,  # Use the media ID from the upload step
                "caption": "Bonne reception.",
                "filename": f"{file_name.capitalize()}"  # Title of the document
            }
        }

        response = requests.post(url, headers=headers, json=data)

        print("Media sent successfully !")

        return response.status_code, response.text

    def delete_media(self, media_id):

        # URL to delete the media
        delete_url = f"https://graph.facebook.com/v20.0/{media_id}"

        # Set up the headers with authorization token
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        # Send the DELETE request
        response = requests.delete(delete_url, headers=headers)

        # Check the response
        if response.status_code == 200:
            print("Media deleted successfully!")
        else:
            print(f"Failed to delete media: {response.status_code}, {response.text}")

if __name__ == "__main__":
    phone_number_id = 458857697302383
    media_path = 'notification_conge.pdf'
    access_token = "EAAMfJJStAz4BOZCknQ0VUznrDXTEKNPKwXJhnae2V1HfTv3ghtgM4NEDfQI4JuxfVDofOUeM7qojXC6NvczKlaXE6T7EY8QYZBggn4TvWC8VxopgpFdZCc4uv8fjwUnodwSujMMEG4oZARRNW4jt0D2O0i22wotbLIq0HZCKjp7KTHqohEZBdTHm2Bavoh8vHOxtE94pSdsiG6rIuulfKmxbltfAaS"

    media = Media(phone_number_id, access_token)
    
    destination_phone_number = "221778577500"

    media_id = media.upload_media(media_path) # 1775586952977377
    response = media.send_media(media_id, media_path, destination_phone_number)
    media.delete_media(media_id)
