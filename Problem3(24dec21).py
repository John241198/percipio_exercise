# Problem 3:
"""
Create a directory with multiple file types - doc, txt, pdf, html
Iteratively open each file with the associated program installed in your system.
For Eg doc to be opened by Microsoft word
"""

import os
import subprocess

# creating directory with multiple files
os.mkdir(r"C:\Users\ELCOT\HCL Python Training\mynewdir")
mypath1 = r"C:\Users\ELCOT\HCL Python Training\mynewdir\file.txt"
mypath2 = r"C:\Users\ELCOT\HCL Python Training\mynewdir\file.pdf"
mypath3 = r"C:\Users\ELCOT\HCL Python Training\mynewdir\file.docx"

with open(mypath1, "w") as f:
    f.write('This is my first line in file.txt which I have created by python')

with open(mypath2, "w") as f:
    f.write("This is my first line in file.pdf which I have created by python")

with open(mypath3, "a") as f:
    f.write("This is my first line in file.docx which I have created by python")


#listing files available in dir
mypath=r"C:\Users\ELCOT\HCL Python Training\mynew_dir"
print("Available files")
for file_path in os.listdir(mypath):
     print(file_path)


#files open on there editor
for file_path in os.listdir(mypath):
    fpath = os.path.join(mypath, file_path)

    if ".txt" in fpath:
        txt_file = r"C:\Windows\notepad.exe"
        file = subprocess.Popen([txt_file, fpath])
        print("text file is open in notepad!......")

    if ".pdf" in fpath:
        pdf_file = r"C:\Program Files (x86)\Adobe\Reader 11.0\Reader\AcroRd32.exe"
        file2 = subprocess.Popen([pdf_file, fpath])
        print("pdf file is open in pdf editor!.....")

    if ".docx" in fpath:
        doc_file = "C:\Program Files\Windows NT\Accessories\wordpad.exe"
        file3 = subprocess.Popen([doc_file, fpath])
        print("Docx file is open in wordpad!......")

