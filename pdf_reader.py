from pypdf import PdfReader
from pdf2image import convert_from_path
import pytesseract

def extract_text_with_ocr(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ""

    for page in pages:
        text += pytesseract.image_to_string(page)

    return text
def extract_text_with_ocr(pdf_path):
    pages = convert_from_path(pdf_path, poppler_path="/opt/homebrew/bin")
    text = ""

    for page in pages:
        text += pytesseract.image_to_string(page)

    return text

def extract_text(pdf_path):
    # Step 1: Try normal extraction
    text = extract_text_normal(pdf_path)

    # Step 2: If text is empty or too short → fallback to OCR
    if len(text.strip()) < 50:
        text = extract_text_with_ocr(pdf_path)

    return text
def extract_text_normal(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text
    
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    all_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            all_text += text + "\n"
    return all_text