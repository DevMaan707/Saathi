import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def preprocess_image(image_path):

    img = cv2.imread(image_path)


    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    _, binary_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return binary_img

def extract_text_from_image(image_path):

    preprocessed_img = preprocess_image(image_path)


    extracted_text = pytesseract.image_to_string(preprocessed_img, lang='eng')

    return extracted_text


image_path = 'C:\\Users\\Aymaan\\Downloads\\test2.jpg'


extracted_text = extract_text_from_image(image_path)


print('Extracted Text:')
print(extracted_text)
