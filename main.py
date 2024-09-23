from payment import Bulletins
from messaging import Media

def save_bulletins_use_case():
    file_name = "bulletins_paie.pdf"
    bulletins = Bulletins(file_name, 3)
    bulletins.save_bulletins()

def get_bulletin_use_case():
    file_name = "bulletins_paie.pdf"
    bulletins = Bulletins(file_name)
    matricule = 30030944
    b = bulletins.get_bulletin(matricule)
    bulletins.save_bulletin(b, f"{matricule}.pdf")

def get_page_use_case():
    file_name = "bulletins_paie.pdf"
    page_num = 20
    bulletins = Bulletins(file_name)
    b = bulletins.get_page(page_num)
    bulletins.save_bulletin(b, f"{page_num}.pdf")

def send_pdf_use_case():
    Media(458857697302383, 
        "EAAMfJJStAz4BOZCknQ0VUznrDXTEKNPKwXJhnae2V1HfTv3"
        "ghtgM4NEDfQI4JuxfVDofOUeM7qojXC6NvczKlaXE6T7EY8Q"
        "YZBggn4TvWC8VxopgpFdZCc4uv8fjwUnodwSujMMEG4oZARR"
        "NW4jt0D2O0i22wotbLIq0HZCKjp7KTHqohEZBdTHm2Bavoh8"
        "vHOxtE94pSdsiG6rIuulfKmxbltfAaS"
    ).send("notification_conge.pdf", "221771332916", "Bon conges!")


if __name__ == '__main__':
    # save_bulletins_use_case()
    # get_bulletin_use_case()
    # get_page_use_case()
    send_pdf_use_case()