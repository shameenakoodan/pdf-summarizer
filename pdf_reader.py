from pypdf import PdfReader
from pdf2image import convert_from_path
import pytesseract
from langdetect import detect

POPPLER_PATH = "/opt/homebrew/bin"  # adjust for Windows/Linux if needed


def extract_text_normal(pdf_path):
    """Extract text using PyPDF (fast, works for digital PDFs)."""
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def extract_text_with_ocr(pdf_path):
    """Fallback OCR for scanned PDFs."""
    pages = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    text = ""

    for page in pages:
        text += pytesseract.image_to_string(page)

    return text


def extract_text(pdf_path):
    """Try normal extraction → fallback to OCR if needed."""
    text = extract_text_normal(pdf_path)

    if len(text.strip()) < 50:  # scanned or image‑based PDF
        text = extract_text_with_ocr(pdf_path)

    return text


def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"
