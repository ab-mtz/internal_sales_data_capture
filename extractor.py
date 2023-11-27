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
data = [

]

def main():
    # Create reader
    reader = easyocr.Reader(['de'])

    # Load image
    image_path = 'images\sample2.jpg'
    
    # Output path 
    filename = "output.csv"

    # extract text
    results = reader.readtext(image_path)
    
    # search for regular expresions
    bestellung = None
    datum = None
    zahlung = None
    for line in results:
        ic(line)
        _, content, _2 = line
        # ic(content)
        bestellung_pattern = r'\bde\d{10}\b'
        date_pattern = r'^\d{2}\.\d{2}\.\d{4}$'
        zahlung_pattern = r'\d*.?\d+ *€'

        # if match := re.search(bestellung_pattern, content):
        #     if bestellung == None:
        #         bestellung = match.group(0)
        #     ic(match)

        # if match := re.search(date_pattern, content):
        #     if datum == None:
        #         datum = validate_date(match.group(0))
        #     ic(match)

        # if match := re.search(zahlung_pattern, content):
        #     zahlung = match.group(0)
        #     ic(match)
        # Define a function to find the first match for a pattern in the text
        

        # Find the first occurrence of each pattern
        bestellung = find_first_match(bestellung_pattern, text)
        date = find_first_match(date_pattern, text)
        zahlung = find_first_match(zahlung_pattern, text)
        if bestellung and datum and zahlung:
            data.append([bestellung, datum, zahlung, current_date])
            bestellung = None
            datum = None
            zahlung = None

    ic(data)
    try:
        # If file already exists
        with open(filename, mode='a+', newline='') as file:
            writer = csv.writer(file)
            file.seek(0, 2)  # Move the cursor to the beginning
            file_empty = file.tell() == 0

            # Create a CSV writer object
            writer = csv.writer(file)

            # Write the header if the file is empty
            if file_empty:
                writer.writerows(header)
                file.flush()

            file.seek(0, 2)

            # Writing the data to the CSV file
            writer.writerows(data)

            if file_empty:
                print(f"The CSV file '{filename}' has been created.")
            else:
                print(f"The CSV file '{filename}' has been updated.")

    except FileNotFoundError:
        # If the file doesn't exist, create a new CSV file
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(header)
            writer.writerows(data)
            print(f"The CSV file '{filename}' has been created.")

    # pack info 
    # conect to google sheet api 

    # instert into to fields

def validate_date(matched):
    ic(matched)
    day, month, year = map(int, matched.split("."))
    if day < 0 or day > 31 or month > 0 or month > 12 or year != datetime.year:
        return f'{matched}(Error)'
def find_first_match(pattern, text):
            match = re.search(pattern, text)
            return match.group(0) if match else None

if __name__ == "__main__":
    main()