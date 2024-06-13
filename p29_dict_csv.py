import csv

def write_dict_to_csv(file_path, data):
    try:
        with open(file_path, 'w', newline='') as csv_file:
            fieldnames = data.keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write the header
            writer.writeheader()

            # Write the data
            writer.writerow(data)

        print(f"Data written to '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred while writing to CSV: {e}")

def read_csv_and_display(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)

            # Display header
            print("Header:", reader.fieldnames)

            # Display content
            for row in reader:
                print(row)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while reading from CSV: {e}")

# Example usage
csv_filename = "example_output.csv"
data_to_write = {"Name": "John", "Age": 30, "Occupation": "Engineer", "Country": "USA"}

# Write dictionary to CSV
write_dict_to_csv(csv_filename, data_to_write)

# Read CSV and display content
read_csv_and_display(csv_filename)
