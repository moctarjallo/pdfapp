from pathlib import Path
from document import Payslip, Leave
from messaging import Media

import pandas as pd

PHONE_NUMBER_ID = 458857697302383
ACCESS_TOKEN = "EAAMfJJStAz4BOZCYd2WOUz7BLkQh7SDbye1ZBfFzbl8UeD2lZAxGEZArPmp1a7J9ZBBirSbAGYq5oiV1I8r1brBvCJznrXrYDNV4uslnRCjRHehmHzMfLFQUGpm4EM7dkMPOHCZAtXLYN5mg9lFcAZCWBXq89T7CRYMzGWBeqYzKBleO4uFz5iYlaAElZCFSMwBm7XZAPXAOM3LQFzvghH4v2CdsrU84ZD"

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

def generate_folder(pdf_path, excel_path, mode="leave"):
    folder_name = Path(pdf_path).stem
    folder = Path(folder_name)
    if not folder.exists():
        folder.mkdir()
    if mode == "leave":
        document = Leave(pdf_path)
    elif mode == "pay":
        document = Payslip(pdf_path)
    df = pd.read_excel(excel_path)
    for matricule in df['Matricule']:
        b = document.get_page_by_matricule(matricule)
        file = Path(f"{folder}/{matricule}.pdf")
        document.save_to_pdf(b, file)
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

def send(pdf_path, excel_path, generate=True, delete=True, mode='leave'):
    """
    pdf_path: either a path to a pdf file or a folder containing individual pdfs
    """
    if generate:
        folder_name = generate_folder(pdf_path, excel_path, mode)
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
