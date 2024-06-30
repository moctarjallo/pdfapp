import os
from PyPDF2 import PdfWriter, PdfReader

class Bulletins():
    def __init__(self, file_name, num_pages):
        self.__in_f = open(file_name, "rb")
        self.pages = PdfReader(self.__in_f).pages[:num_pages]

    def __len__(self):
        return len(self.pages)

    def get_matricule(self, i):
        page = self.pages[i]
        page_text = page.extract_text()
        ligne_matricule = page_text.split('\n')[6]
        matricule = int(ligne_matricule.split()[2])
        return matricule

    def save_bulletin(self, page, file_name):
        writer = PdfWriter()
        writer.add_page(page)
        with open(f"{file_name}.pdf", "wb") as output_pdf:
            writer.write(output_pdf)

    def save_bulletins(self):
        for i in range(len(self)):
            matricule = self.get_matricule(i)
            self.save_bulletin(self.pages[i], f"{matricule}")
        self.__in_f.close()


def get_bulletin(matricule, bulletins):
    return [bulletin for bulletin in bulletins if bulletin.get(matricule)][0]

def main():
    file_name = "bulletins_paie.pdf"
    bulletins = Bulletins(file_name, 3)
    bulletins.save_bulletins()

if __name__ == '__main__':
    main()
