from PIL import Image
import easyocr 
from icecream import ic
import re


def main():
    # Create reader
    reader = easyocr.Reader(['de'])

    # Load image
    image_path = 'images\sample1.jpg'
    # extract text
    results = reader.readtext(image_path)
    # ic(results)
    # search for regular expresions
    for line in results:
        ic(line)
        # Bestellungs nummer
        # pattern = 'de\d*'
        # datum
        # pattern = '\d+\.\d+\.\d+'
        # €
        # pattern = '\d*.?\d+ *€'
    # pack info 
    # conect to google sheet api 
    # instert into to fields

if __name__ == "__main__":
    main()