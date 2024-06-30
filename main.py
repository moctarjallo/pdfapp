import os
from PyPDF2 import PdfWriter, PdfReader, PdfMerger

def read_bulletins():
    with open("bulletins_paie.pdf", 'rb') as infile:
        pages = PdfReader(infile).pages

        def parse_bulletin(page):
            page_text = page.extract_text()
            ligne_matricule = page_text.split('\n')[6]
            matricule = int(ligne_matricule.split()[2])
            return {matricule: page}

        return [parse_bulletin(page) for page in pages]

def get_bulletin(matricule, bulletins):
    return [bulletin for bulletin in bulletins if bulletin.get(matricule)][0]

def save_bulletin(page, file_name):
    writer = PdfWriter()
    writer.add_page(page)
    with open("%s-page.pdf" % (file_name), "wb") as output_pdf:
        writer.write(output_pdf)

def save_bulletins(file_name):
    with open(file_name, "rb") as in_f:
        pages = PdfReader(in_f).pages
        for i in range(0, 2):
            page = pages[i]
            save_bulletin(page, f"{file_name}-{i}")

def merge_pdf(file_name):
    # Merge the split PDF files
    merge_pdf = PdfMerger()

    for i in range(0, 2):
        merge_pdf.append(open("%s-page%s.pdf" % (file_name, i), "rb"))

    with open("merged_%s" % file_name, "wb") as output_pdf:
        merge_pdf.write(output_pdf)

if __name__ == '__main__':
    # bulletins = read_bulletins()
    # b = get_bulletin(30030654, bulletins)
    file_name = "bulletins_paie.pdf"
    save_bulletins(file_name)
    # merge_pdf(file_name)
    # print(b)