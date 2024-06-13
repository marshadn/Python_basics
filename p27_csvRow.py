import csv

def read_csv_and_print(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            
            for row in reader:
                print(row)
                
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
csv_filename = "exampleRow.csv"
read_csv_and_print(csv_filename)
