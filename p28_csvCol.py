import csv

def read_specific_columns(file_path, columns):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            
            # Find the index of each specified column
            header = next(reader)
            column_indices = [header.index(column) for column in columns]
            
            # Print the header of selected columns
            selected_header = [header[i] for i in column_indices]
            print(selected_header)

            # Print the content of selected columns
            for row in reader:
                selected_data = [row[i] for i in column_indices]
                print(selected_data)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print("Error: One or more specified columns not found in the CSV file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
csv_filename = "exampleCol.csv"
selected_columns = ["Name", "Occupation"]

read_specific_columns(csv_filename, selected_columns)
