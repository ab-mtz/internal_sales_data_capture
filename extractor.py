from PIL import Image
import easyocr 
from icecream import ic
import re


def main():
    # Create reader
    reader = easyocr.Reader(['de'])

    # Load image
    image_path = 'images\sample-text-1.jpg'
    # extract text
    results = reader.readtext(image_path)
    ic(results)
    # search for regular expresions
        # Bestellungs nummer
        # pattern = 'bestellung'
        # datum
        # pattern = '\d+\.\d+\.\d+'
        # €
        # pattern = '\d*.?\d+ *€'
    # pack info 
    # conect to google sheet api 
    # instert into to fields

if __name__ == "__main__":
    main()