from .document import Document

class Leave(Document):
    def get_matricule(self, i):
        page = self.pages[i]
        page_text = page.extract_text()
        ligne_matricule = page_text.split('\n')[14]
        matricule_pos = ligne_matricule.split().index('Mle:')
        matricule = int(ligne_matricule.split()[matricule_pos+1])
        return matricule
