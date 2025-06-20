from langchain.agents import Tool
from PIL import Image
import pytesseract

def ocr_function(image_path: str) -> str:
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

ocr_tool = Tool(
    name="OCR",
    func=ocr_function,
    description="Extract text from images via OCR."
)
