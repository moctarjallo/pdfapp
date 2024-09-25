from pathlib import Path
from payment import Leave
from messaging import Media

import pandas as pd

PHONE_NUMBER_ID = 458857697302383
ACCESS_TOKEN = "EAAMfJJStAz4BO10Xyc4sMeEqPVr8njV8heHoRLZCxJSUNC6NgITHDg7IzAdcmGWJEvyemsHRrtDAsnz2X76lZAlLGxZAyrFZBZCCUE6gn0aqU7MnemOy2agV2IfGLQiP50r81vPlYy5s1YpKHYZAI4cNLVY7VBZCcc3kZBSBo6zd9DgpX4aLCznzyy0ZBP5em9ZAlDgWqe5nWI585rZCRjRn8OZBLsscbeQZD"

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

def generate(pdf_path, excel_path):
    folder_name = Path(pdf_path).stem
    folder = Path(folder_name)
    if not folder.exists():
        folder.mkdir()
    leaves = Leave(pdf_path)
    df = pd.read_excel(excel_path)
    for matricule in df['Matricule']:
        b = leaves.get_bulletin(matricule)
        file = Path(f"{folder}/{matricule}.pdf")
        leaves.save_bulletin(b, file)

def delete(folder_name):
    folder = Path(folder_name)
    for file in folder.iterdir():
        file.unlink()
    folder.rmdir()

def send(folder_name, excel_path):
    media = Media(PHONE_NUMBER_ID, ACCESS_TOKEN)
    df = pd.read_excel(excel_path)
    for matricule, telephone in zip(df['Matricule'], df['Telephone'].str.replace(' ', '')):
        media.send(f"{folder_name}/{matricule}.pdf", telephone)

if __name__ == '__main__':
    # generate('C:\\Users\\HP\kajande\\frontend\\python\\api\\pdfapp\\notification_conge.pdf', 'recipients.xlsx')
    send('notification_conge', 'recipients.xlsx')
    # delete('notification_conge')
