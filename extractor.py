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
    bestellung = ""
    datum = ""
    zahlung = ""
    for line in results:
        # ic(line)
        _, content, _2 = line
        ic(content)
        bestellung_pattern = r'de\d*'
        date_pattern = r'\d+\.\d+\.\d+'
        zahlung_pattern = r'\d*.?\d+ *€'
        if content == re.search(bestellung_pattern, content):
            bestellung = content
        if content == re.search(date_pattern, content):
            datum == content
        if content == re.search(zahlung_pattern, content):
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