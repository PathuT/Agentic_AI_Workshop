from PIL import Image
import pytesseract
from pyzbar.pyzbar import decode
import fitz

def extract_text_from_image(img: Image.Image) -> str:
    return pytesseract.image_to_string(img)

def scan_qr_from_image(img: Image.Image) -> str:
    decoded = decode(img)
    if decoded:
        return decoded[0].data.decode("utf-8")
    return "No QR found"

def extract_text_from_pdf(file) -> str:
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)
