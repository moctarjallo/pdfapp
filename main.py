import os
from PyPDF2 import PdfWriter, PdfReader


def get_matricule(page):
    page_text = page.extract_text()
    ligne_matricule = page_text.split('\n')[6]
    matricule = int(ligne_matricule.split()[2])
    return matricule

def get_bulletin(matricule, bulletins):
    return [bulletin for bulletin in bulletins if bulletin.get(matricule)][0]

def save_bulletin(page, file_name):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"{file_name}.pdf", "wb") as output_pdf:
        writer.write(output_pdf)

def save_bulletins(file_name):
    with open(file_name, "rb") as in_f:
        pages = PdfReader(in_f).pages
        for page in pages[:3]:
            matricule = get_matricule(page)
            save_bulletin(page, f"{matricule}")

def main():
    file_name = "bulletins_paie.pdf"
    save_bulletins(file_name)

if __name__ == '__main__':
    main()
