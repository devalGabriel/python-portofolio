import pytesseract
import cv2

def extract_receipt_text(image_path):
    # Poți adapta calea către tesseract dacă nu e în PATH:
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Preprocesare simplă, poți adăuga threshold dacă e nevoie
    text = pytesseract.image_to_string(gray, lang='ron+eng')
    return text
