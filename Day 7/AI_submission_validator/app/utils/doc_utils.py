from PIL import Image
import pytesseract
import fitz  # PyMuPDF
import cv2
import numpy as np

def extract_text_from_image(img: Image.Image) -> str:
    return pytesseract.image_to_string(img)

def scan_qr_from_image(img: Image.Image) -> str:
    # Convert PIL Image to OpenCV image
    cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(cv_img)
    return data if data else "No QR found"

def extract_text_from_pdf(file) -> str:
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)
