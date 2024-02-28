import re
import cv2
import pytesseract as tess
path = (r"C:\Users\10\AppData\Local\Tesseract-OCR\tesseract.exe")
tess.pytesseract.tesseract_cmd = path


png = "m.png"
text = tess.image_to_string(png)
text.replace(" ", "")
pattern = re.compile("([0-9][=+-/*])")
equations = [x for x in text if bool(re.match(pattern, x))]

print(re.findall(r'(.*)', str(text))[0])