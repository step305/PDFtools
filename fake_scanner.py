from pdf2image import convert_from_path
import tkinter as tk
from tkinter import filedialog
import os
import cv2
from PIL import Image


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames()
    print(file_paths)

    for file_path in file_paths:
        _, pdf_name = os.path.split(file_path)
        dir_path = os.path.dirname(file_path)
        new_dir_path = os.path.join(dir_path, 'scanned')
        if not os.path.exists(new_dir_path):
            os.mkdir(new_dir_path)
        new_pdf_path = os.path.join(new_dir_path, pdf_name.split('.')[0] + '.pdf')
        new_img_path = os.path.join(new_dir_path, pdf_name.split('.')[0] + '.png')
        print(new_pdf_path)
        pages = convert_from_path(file_path, dpi=600, poppler_path='poppler\\poppler-22.04.0\\Library\\bin')
        pages[0].save(file_path, 'PNG')
        img = cv2.imread(file_path)
        img = cv2.resize(img, (1240, 1754))
        cv2.imwrite(new_img_path, img)

        img = Image.open(new_img_path)
        img.convert('RGB')
        img.save(new_pdf_path)

        os.remove(new_img_path)
