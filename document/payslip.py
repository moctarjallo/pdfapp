from .document import Document

class Payslip(Document):
    def get_matricule(self, i):
        page = self.pages[i]
        page_text = page.extract_text()
        ligne_matricule = page_text.split('\n')[6]
        matricule = int(ligne_matricule.split()[2])
        return matricule
