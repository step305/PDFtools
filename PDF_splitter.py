from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk
from tkinter import filedialog


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    print(file_path)

    inputpdf = PdfFileReader(open(file_path, "rb"))
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("split_out\\split_out-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
