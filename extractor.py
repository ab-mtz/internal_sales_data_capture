from PIL import Image
import easyocr 
from icecream import ic
import re
import csv
from datetime import datetime
import sys, os


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
    
    # Load images from the current directory with jpg or jpeg extension
    folder_path = "to_process"
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.jpg', '.jpeg'))]


    for image_file in image_files:
        # Load image
        image_path = image_file


        # Header
        header = [
            ["Bestellung", "Datum", "Zahlung", "Captured at"]
        ]
        # Empty data variable list of lists
        data = [

        ]

        # Create reader
        reader = easyocr.Reader(['de'])

        # Load image
        # image_path = 'images\sample2.jpg'
        
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
            _, content, _2 = line
            if not bestellung:
                bestellung = search_pattern(bestellung_pattern, content)
            if not datum:
                _datum = search_pattern(datum_pattern, content)
                if _datum:
                    datum = validate_date(_datum)
            if not zahlung:
                zahlung = search_pattern(zahlung_pattern, content)


    # Append the data to data variable
            if bestellung and datum and zahlung:

                # ic(data)
                data.append([bestellung, datum, zahlung, current_date])
                bestellung = None
                datum = None
                zahlung = None

        if not data:
            sys.exit("=" * 20,"We haven´t found new data to store in your csv file","=" * 20)
        else:
            # Check if data already saved in file
            check_values_in_csv(data, filename)
            # ic(data)

            save_data_to_file(header, data, filename)


def validate_date(_datum):
    ic(_datum)
    _day, _month, _year = map(int, _datum.split("."))
    current_datetime = datetime.now()
    current_year = current_datetime.year
    ic(current_year)
    if _year < 99:
        _year += 2000
        ic(_year)
        ic(datetime.year)
    if _day < 1 or _day > 31 or _month < 1 or _month > 12 or _year != current_year:
        return f'{_datum}(Error)'
    else:
        return _datum

def search_pattern(pattern, content):
    if match := re.search(pattern, content):
        # ic(match)
        return match[0]
                
def save_data_to_file(header, data, filename):
    if not data:
        print("=" * 20, "We haven't found new data to store in your csv file", "=" * 20)
    else:
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
                    print("=" * 20, f"The CSV file '{filename}' has been created.", "=" * 20)
                else:
                    print("=" * 20, f"The CSV file '{filename}' has been updated.", "=" * 20)

        except FileNotFoundError:
            # If the file doesn't exist, create a new CSV file
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(header)
                writer.writerows(data)
                print("=" * 20, f"The CSV file '{filename}' has been created.", "=" * 20)


def check_values_in_csv(data, filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            # Skip the header
            next(reader, None)
            
            for entry in data:
                value = entry[0]
                # ic(value)
                
                # Check each row in the CSV file
                for row in reader:
                    # Assuming the value you're checking is in the first column
                    if value == row[0]:
                        print("=" * 20, f"The value '{value}' already exist in the CSV file.", "=" * 20)
                        data.remove(entry)
                        break  # Assuming each value appears only once in the CSV
    except FileNotFoundError:
        print("=" * 20, "CSV file not found.", "=" * 20)
        pass


if __name__ == "__main__":
    main()