from PIL import Image
import pytesseract
import numpy as np
from pytesseract import Output
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

filename = 'Testing Material/2.png'
img = np.array(Image.open(filename))
text = pytesseract.image_to_string(img)

print(text)

results = pytesseract.image_to_data(img, output_type=Output.DICT)

for i in range(0, len(results["text"])):
    x = results["left"][i]
    y = results["top"][i]

    w = results["width"][i]
    h = results["height"][i]
    text = results["text"][i]
    conf = int(results["conf"][i])
    if conf > 40:
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

cv2.imshow(" ", img)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
