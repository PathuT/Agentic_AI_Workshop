from PIL import Image
import pytesseract
from pyzbar.pyzbar import decode

def extract_text_from_image(image: Image.Image) -> str:
    return pytesseract.image_to_string(image)

def scan_qr_from_image(image: Image.Image) -> str:
    decoded_objs = decode(image)
    if decoded_objs:
        return decoded_objs[0].data.decode('utf-8')
    return "No QR found"
