import pytesseract
from PIL import Image
import sys
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract"

def autoRecognize():
    image=Image.open(sys.path[1]+"/educationSystem/verifyImage/verifyCode.jpg")
    return pytesseract.image_to_string(image)