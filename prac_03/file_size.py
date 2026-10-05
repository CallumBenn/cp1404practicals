"""
CP1404/CP5632 - Practical 03
Callum Bennett
"""

def main():
    """Get file name and print number of lines within file"""
    filename = input("Filename: ")
    while filename != "":
        try:
            file = open(filename, 'r')
            print(f"{filename} has {count_lines_in_file(file)} lines")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Filename: ")



def count_lines_in_file(file):
    """Count number of lines in specified file"""
    number_of_lines = 0
    for line in file:
        number_of_lines += 1
    return number_of_lines


main()