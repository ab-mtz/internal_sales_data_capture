from PIL import Image
import easyocr 
from icecream import ic
import re
import csv
from datetime import datetime
import sys



def main():
    #Dates variables
    current_datetime = datetime.now()
    year = current_datetime.year
    month = current_datetime.month
    day = current_datetime.day
    current_date = f'{day}.{month}.{year}'


    # Regex patterns
    bestellung_pattern = r'\bde\d{10}\b'
    datum_pattern = r'\b\d{1,2}\.\d{1,2}\.\d{2,4}\b'
    zahlung_pattern = r'\d*.?\d+ *€'

    header = [
        # Header
        ["Bestellung", "Datum", "Zahlung", "Captured at"]
    ]
    data = [

    ]
    # Create reader
    reader = easyocr.Reader(['de'])

    # Load image
    image_path = 'images\sample4.jpeg'
    
    # Output path 
    filename = "output.csv"

    # extract text
    results = reader.readtext(image_path)
    
    # Variables to append
    bestellung = None
    datum = None
    zahlung = None

    # Search for regular expresions
    
    for line in results:
        # ic(line)
        _, content, _2 = line
        # ic(content)
        if not bestellung:
            bestellung = search_pattern(bestellung_pattern, content)
        ic(bestellung)
        if not datum:
            datum = search_pattern(datum_pattern, content) 
        ic(datum)
        if not zahlung:
            zahlung = search_pattern(zahlung_pattern, content)
        ic(zahlung)

# Old code
        # if match := re.search(bestellung_pattern, content):
        #     if bestellung is None:
        #         bestellung = match.group(0)
        #         ic(match.group(0))
        #     ic(match)

        # if match := re.search(datum_pattern, content):
        #     if datum is None:
        #         datum = validate_date(match.group(0))
        #         ic(match.group(0))

        #     ic(match)

        # if match := re.search(zahlung_pattern, content):
        #     zahlung = match.group(0)
        #     ic(match)

# Append the data to data variable
        if bestellung and datum and zahlung:
            ic(data)
            data.append([bestellung, datum, zahlung, current_date])
            bestellung = None
            datum = None
            zahlung = None

    if not data:
        sys.exit("No data found")
    else:
        save_data_to_file(data, filename)

    ic(data)

    # pack info 
    # conect to google sheet api 

    # instert into to fields

def validate_date(matched):
    ic(matched)
    day, month, year = map(int, matched.split("."))
    if day < 0 or day > 31 or month > 0 or month > 12 or year != datetime.year:
        return f'{matched}(Error)'

def search_pattern(pattern, content):
    if match := re.search(pattern, content):
        ic(match)
        return match[0]
                
def save_data_to_file(data, filename):
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

if __name__ == "__main__":
    main()