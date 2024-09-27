from pathlib import Path
from document import Payslip, Leave
from messaging import Media

import pandas as pd

PHONE_NUMBER_ID = 458857697302383
ACCESS_TOKEN = "EAAMfJJStAz4BOy2mlMtNRDYdFZBsBszaZBOSfZBGfgh3XZCGkmuNZAZAB5Wa2kxpLonMo3hFL2exthGN6wCnR9weV7IetuiLe5zHjZCtayfZBPTDKRVNgNlc2p7y2lKF6ySjpsZBCEQtx42ItJn7meefhc7hpx2nJddB6bHF31ad4XzHS6wjxAKN1Fj4t2TSWmJXA4QOrY2LqeHOTbg47DFitS6qQnmYZD"

"""
Add these 3 general and separated use cases:
backend:
    1. generate(folder_name, excel_path) -> generates the PDF out of the EXCEL definitions
                RETURNS a folder of all generated files
    2. send(folder_name, excel_path) -> send the previously generate folder 
                RETURNS a progress bar (tqdm?)
    3. delete(folder_name, excel_path) -> deletes all files in folder, based on excel params
                RETURNS progress bar (tqdm?)
"""

def generate_folder(pdf_path, excel_path):
    folder_name = Path(pdf_path).stem
    folder = Path(folder_name)
    if not folder.exists():
        folder.mkdir()
    leaves = Leave(pdf_path)
    df = pd.read_excel(excel_path)
    for matricule in df['Matricule']:
        b = leaves.get_page_by_matricule(matricule)
        file = Path(f"{folder}/{matricule}.pdf")
        leaves.save_to_pdf(b, file)
    return folder_name

def delete_folder(folder_name):
    folder = Path(folder_name)
    for file in folder.iterdir():
        file.unlink()
    folder.rmdir()

def send_folder(folder_name, excel_path):
    media = Media(PHONE_NUMBER_ID, ACCESS_TOKEN)
    df = pd.read_excel(excel_path)
    for matricule, telephone in zip(df['Matricule'], df['Telephone'].str.replace(' ', '')):
        media.send(f"{folder_name}/{matricule}.pdf", telephone)

def send(pdf_path, excel_path, generate=True, delete=True):
    """
    pdf_path: either a path to a pdf file or a folder containing individual pdfs
    """
    if generate:
        folder_name = generate_folder(pdf_path, excel_path)
    else:
        folder_name = pdf_path
    send_folder(folder_name, excel_path)
    if delete:
        delete_folder(folder_name)

if __name__ == '__main__':
    # generate_folder('C:\\Users\\HP\kajande\\frontend\\python\\api\\pdfapp\\notification_conge.pdf', 'recipients.xlsx')
    # send_folder('notification_conge', 'recipients.xlsx')
    # delete_folder('notification_conge')
    send('notification_conge.pdf', 'recipients.xlsx')
