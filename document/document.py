import os
from PyPDF2 import PdfWriter, PdfReader

class Document():
    def __init__(self, file_name, num_pages=None):
        self.__in_f = open(file_name, "rb")
        if not num_pages:
            num_pages = -1
        self.pages = PdfReader(self.__in_f).pages[:num_pages]

    def __len__(self):
        return len(self.pages)

    def get_matricule(self, i):
        raise NotImplemented("You should override and implement this method.")

    def get_page_by_matricule(self, matricule):
        for i, page in enumerate(self.pages):
            if self.get_matricule(i) == matricule:
                return page
        raise Exception(f"Matricule {matricule} is not found.")

    def get_page_by_num(self, page_num):
        for i, page in enumerate(self.pages):
            if i == page_num-1:
                return page
        raise Exception(f"Page {page_num} is not found.")

    def save_to_pdf(self, page, file_name):
        writer = PdfWriter()
        writer.add_page(page)
        with open(f"{file_name}", "wb") as output_pdf:
            writer.write(output_pdf)

    def save_pages_to_pdf(self):
        for i in range(len(self)):
            matricule = self.get_matricule(i)
            self.save_to_pdf(self.pages[i], f"{matricule}.pdf")
        self.__in_f.close()
