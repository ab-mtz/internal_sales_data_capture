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
        # ic(line)
        _, content, _2 = line
        ic(content)
        bestellung_pattern = 'de\d*'
        date_pattern = '\d+\.\d+\.\d+'
        zahlung_pattern = '\d*.?\d+ *€'
        if content == bestellung_pattern:
            bestellung = content
        if content == date_pattern:
            datum == content
        if content == zahlung_pattern:
            zahlung = content
    ic(bestellung, datum, zahlung)
        
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