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

def save_bulletin(file_name):
    if not os.path.isfile(file_name):
        print(f"The file {file_name} does not exist.")
    else:
        inputpdf = PdfReader(open(file_name, "rb"))

        for i in range(0, 6):
            writer = PdfWriter()
            writer.add_page(inputpdf.pages[i])
            with open("%s-page%s.pdf" % (file_name, i), "wb") as output_pdf:
                writer.write(output_pdf)

        # Merge the split PDF files
        merge_pdf = PdfMerger()

        for i in range(0, 6):
            merge_pdf.append(open("%s-page%s.pdf" % (file_name, i), "rb"))

        with open("merged_%s" % file_name, "wb") as output_pdf:
            merge_pdf.write(output_pdf)

if __name__ == '__main__':
    # bulletins = read_bulletins()
    # b = get_bulletin(30030654, bulletins)
    save_bulletin("bulletins_paie.pdf")
    # print(b)