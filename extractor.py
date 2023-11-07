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
        date_pattern = r'^\d{2}\.\d{2}\.\d{4}$'
        zahlung_pattern = r'\d*.?\d+ *€'
        if match := re.search(bestellung_pattern, content):
            bestellung = match[0]
        if match := re.search(date_pattern, content):
            datum = match[0]
        if match := re.search(zahlung_pattern, content):
            zahlung = match[0]
    ic(bestellung, datum, zahlung)
   
    # pack info 
    # conect to google sheet api 
    
    # instert into to fields

if __name__ == "__main__":
    main()