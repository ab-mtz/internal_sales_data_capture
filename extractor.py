from PIL import Image
import easyocr 
from icecream import ic
import re
import csv
from datetime import datetime

current_datetime = datetime.now()
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
current_date = f'{day}.{month}.{year}'

header = [
    # Header
    ["Bestellung", "Datum", "Zahlung","Captured at"]
]
data = []

def main():
    # Create reader
    reader = easyocr.Reader(['de'])

    # Load image
    image_path = 'images\sample2.jpg'

    # extract text
    results = reader.readtext(image_path)
    
    # search for regular expresions
    bestellung = ""
    datum = ""
    zahlung = ""
    for line in results:
        # ic(line)
        _, content, _2 = line
        # ic(content)
        bestellung_pattern = r'de\d*'
        date_pattern = r'^\d{2}\.\d{2}\.\d{4}$'
        zahlung_pattern = r'\d*.?\d+ *€'

        if match := re.search(bestellung_pattern, content):
            bestellung = match[0]
            ic(match)

        if match := re.search(date_pattern, content):
            datum = validate_date(match[0])
            ic(match)

        if match := re.search(zahlung_pattern, content):
            zahlung = match[0]
            ic(match)

        if bestellung and datum and zahlung:
            data.append([bestellung, datum, zahlung, current_date])
            bestellung = ""
            datum = ""
            zahlung = ""

    filename = "output.csv"

    
    # try:
    # If file already exists
    with open(filename, mode='a+', newline='') as file:
        writer = csv.writer(file)
        file.seek(0, 2)  # Move the cursor to the end of the file
        file_empty = file.tell() == 0

        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the header if the file is empty
        if file_empty:
            writer.writerow(header)
            # Writing the data to the CSV file
            writer.writerows(data)
            print(f"The CSV file '{filename}' has been created.")
        else:
            writer.writerows(data)
            print(f"The CSV file '{filename}' has been updated.")

    # except FileNotFoundError:
    #     # If the file doesn't exist, create a new CSV file
    #     with open(filename, 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(header)
    #         writer.writerows(data)

    # pack info 
    # conect to google sheet api 

    # instert into to fields

def validate_date(matched):
    ic(matched)
    day, month, year = map(int, matched.split("."))
    if day < 0 or day > 31 or month > 0 or month > 12 or year != datetime.year:
        return f'{matched}(Error)'


if __name__ == "__main__":
    main()