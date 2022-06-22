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
        new_img_path = os.path.join('beautify', pdf_name.split('.')[0] + '.png')
        new_pdf_path = os.path.join('beautify', pdf_name.split('.')[0] + '.pdf')
        print(os.path.dirname(file_path), pdf_name, new_img_path)
        pages = convert_from_path(file_path, dpi=600, poppler_path='poppler\\poppler-22.04.0\\Library\\bin')
        pages[0].save(new_img_path, 'PNG')
        img = cv2.imread(new_img_path)
        alpha = 1.2  # Contrast control (1.0-3.0)
        beta = 30  # Brightness control (0-100)

        enhanced_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

        cv2.imwrite(new_img_path, enhanced_img)

        img = Image.open(new_img_path)
        img.convert('RGB')
        img.save(new_pdf_path)

        os.remove(new_img_path)
