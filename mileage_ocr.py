import cv2
import pytesseract
import numpy as np
import re

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    _, thresh_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh_image

def extract_mileage(image_path):
    processed_image = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_image)
    return parse_mileage(text)

def parse_mileage(text):
    numbers = re.findall(r'\d+', text)
    if numbers:
        return max(map(int, numbers))
    return None