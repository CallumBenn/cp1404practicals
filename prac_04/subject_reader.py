"""
CP1404/CP5632 - Practical 04
Callum Bennett
"""
from os.path import sep

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    file_contents = load_file_contents(FILENAME)
    # print(data)
    display_subject_details(file_contents)


def load_file_contents(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    file_output = []
    input_file = open(filename)
    for line in input_file:
        parts = line.split(',')  # Separate the data into its parts
        file_contents = [parts[0], parts[1], int(parts[2])]
        file_output.append(file_contents)  # Append line to variable
    input_file.close()
    return file_output


def display_subject_details(file_contents):
    for line in file_contents:
        print(f"{line[0]} is taught by {line[1]} and has {line[2]} students")


"""
    print(line)  # See what a line looks like
    print(repr(line))  # See what a line really looks like
    line = line.strip()  # Remove the \n
    parts = line.split(',')  # Separate the data into its parts
    print(parts)  # See what the parts look like (notice the integer is a string)
    # Make the number an integer as part of a new, poorly named, list
    data = [parts[0], parts[1], int(parts[2])]
    print(data)  # See if that worked
    print("----------")
"""

main()
