from PIL import Image
from pytesseract import pytesseract

# Define path to tesseract.exec
path_tesseract = r'C:\Users\abmtz\AppData\Local\Programs\Tesseract-OCR'

path_image = 'images\sample-text-1.jpg'

# Point tesseract_cmd to tesseract.exe
pytesseract.tesseract_cmd = path_tesseract


def main():
    # Read image
    img = Image.open(path_image)
    # Extract text 
    text = pytesseract.image_to_string(img)

    print(text)
    # run tesseract
    # extract text
    # search for regular expresions
        # Bestellungs nummer
        # datum
        # €
    # pack info 
    # conect to google sheet api 
    # instert into to fields

if __name__ == "__main__":
    main()