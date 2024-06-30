import os
from PyPDF2 import PdfWriter, PdfReader

class Bulletins():
    def __init__(self, file_name, num_pages=None):
        self.__in_f = open(file_name, "rb")
        if not num_pages:
            num_pages = -1
        self.pages = PdfReader(self.__in_f).pages[:num_pages]

    def __len__(self):
        return len(self.pages)

    def get_matricule(self, i):
        page = self.pages[i]
        page_text = page.extract_text()
        ligne_matricule = page_text.split('\n')[6]
        matricule = int(ligne_matricule.split()[2])
        return matricule

    def get_bulletin(self, matricule):
        for i, page in enumerate(self.pages):
            if self.get_matricule(i) == matricule:
                return page

    def get_page(self, page_num):
        for i, page in enumerate(self.pages):
            if i == page_num-1:
                return page

    def save_bulletin(self, page, file_name):
        writer = PdfWriter()
        writer.add_page(page)
        with open(f"{file_name}", "wb") as output_pdf:
            writer.write(output_pdf)

    def save_bulletins(self):
        for i in range(len(self)):
            matricule = self.get_matricule(i)
            self.save_bulletin(self.pages[i], f"{matricule}.pdf")
        self.__in_f.close()

def main():
    file_name = "bulletins_paie.pdf"
    bulletins = Bulletins(file_name, 3)
    bulletins.save_bulletins()

def get_bulletin_use_case():
    file_name = "bulletins_paie.pdf"
    bulletins = Bulletins(file_name)
    b = bulletins.get_bulletin(30030925)
    bulletins.save_bulletin(b, "30030925.pdf")

def get_page_use_case():
    file_name = "bulletins_paie.pdf"
    page_num = 20
    bulletins = Bulletins(file_name)
    b = bulletins.get_page(page_num)
    bulletins.save_bulletin(b, f"{page_num}.pdf")

if __name__ == '__main__':
    # main()
    # get_bulletin_use_case()
    get_page_use_case()