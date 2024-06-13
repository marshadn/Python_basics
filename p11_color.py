# def main():
#     # Get color names from the user
#     color_input = input("Enter comma-separated color names: ")

#     # Split the input into a list of color names
#     colors = [color.strip() for color in color_input.split(',')]

#     # Display the first and last colors
#     if colors:
#         print(f"First color: {colors[0]}")
#         print(f"Last color: {colors[-1]}")
#     else:
#         print("No colors entered.")

# if __name__ == "__main__":
#     main()
c=input("Enter colours separated by comma:")
w=c.split(',')
print("First Color:",w[0])
print("Last Color:",w[-1])
