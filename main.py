from payment import Bulletins

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

if __name__ == '__main__':
    # save_bulletins_use_case()
    # get_bulletin_use_case()
    get_page_use_case()