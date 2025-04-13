from docx import Document
from pdf2image import convert_from_path
import pytesseract
import cv2
import numpy as np

def extract_text(file):
    if file.name.endswith(".docx"):
        return extract_text_from_word(file)
    elif file.name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    else:
        return []

def extract_text_from_word(doc_file):
    # Your existing Word text extractor code
    pass

def extract_text_from_pdf(file, lang='eng', max_pages=5):
    # Your PDF OCR code
    pass
