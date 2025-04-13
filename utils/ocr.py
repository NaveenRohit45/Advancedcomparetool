from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image

def ocr_pdf(file):
    images = convert_from_bytes(file.read())
    text = "\n".join(pytesseract.image_to_string(img) for img in images)
    return text
