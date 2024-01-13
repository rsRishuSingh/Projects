from PyPDF2 import PdfWriter   # first we need to install PyPDF2 
import os

merger = PdfWriter()

files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("DTU1merged.pdf")
merger.close()