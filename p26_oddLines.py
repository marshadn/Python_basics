def copy_odd_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
            lines = in_file.readlines()
            odd_lines = [line for index, line in enumerate(lines, 1) if index % 2 != 0]
            out_file.writelines(odd_lines)
            print(f"Odd lines copied from '{input_file}' to '{output_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_filename = "input.txt"
output_filename = "output.txt"

copy_odd_lines(input_filename, output_filename)
