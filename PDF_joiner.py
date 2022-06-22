from PyPDF2 import PdfFileMerger, PdfFileReader
import tkinter as tk
from tkinter import filedialog


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames()
    print(file_paths)

    merger = PdfFileMerger()
    for file_name in file_paths:
        merger.append(PdfFileReader(open(file_name, 'rb')))
    merger.write("join_out\\output.pdf")
