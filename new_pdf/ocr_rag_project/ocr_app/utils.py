# ocr_app/utils.py

import os
from django.conf import settings
from pdf2image import convert_from_path
import easyocr

# Initialize EasyOCR reader
reader = easyocr.Reader(["en"])


def handle_uploaded_file(pdf_file):
    file_path = os.path.join(settings.MEDIA_ROOT, "pdfs", pdf_file.name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as f:
        for chunk in pdf_file.chunks():
            f.write(chunk)
    return file_path


def clean_up_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def extract_text_with_easyocr(pdf_path):
    text = ""
    images = convert_from_path(pdf_path)
    for image in images:
        results = reader.readtext(image)
        text += " ".join([result[1] for result in results])
    return text
