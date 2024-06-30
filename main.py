from PyPDF2 import PdfReader

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

if __name__ == '__main__':
    bulletins = read_bulletins()
    b = get_bulletin(30030654, bulletins)
    print(b)