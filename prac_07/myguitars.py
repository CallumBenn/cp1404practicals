"""
CP1404/CP5632 - Practical 07
Callum Bennett

Estimate: 35 minutes
Actual: 60 minutes
"""

from typing import Any
from guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""
    in_file = import_file('guitars.csv')
    guitars = format_from_csv(in_file)
    new_guitars = get_guitar()
    append_file('guitars.csv', new_guitars)
    new_guitars = format_from_list(new_guitars)
    guitars = append_guitars(guitars, new_guitars)
    display_list(guitars)
    in_file.close()


def import_file(filename):
    file = open(filename, 'r')
    return file

def append_file(filename, data):
    file = open(filename, 'a')
    for line in data:
        item = ",".join(str(i) for i in line)
        print(item, file=file)


def append_guitars(guitars, new_guitars):
    """Append new guitars to list of guitars, then sort list."""
    for guitar in new_guitars:
        guitars.append(guitar)
    guitars.sort()
    return guitars


def display_list(data):
    """Print items in list."""
    for line in data:
        print(line)


def get_guitar():
    """Get and return guitar name, year and cost"""
    guitars = []
    while True:
        try:
            name = input("Name: ")
            if name == "":
                break
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
        except ValueError:
            break
        guitars.append([name, year, cost])
        print(f"{name} ({year}) : ${cost:.2f} added.")
    if guitars == []:
        return None
    else:
        return guitars


def format_from_csv(file):
    """Return list formatted using Guitar class from csv-formatted lines (E.g.: Guitar,Year,Cost)."""
    guitars = []
    for line in file:
        parts = line.strip().split(',')
        parts[1] = int(parts[1])
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
    return guitars


def format_from_list(item):
    """Return list formatted using Guitar class from list."""
    # Formatting all data entries using 'format_csv' would have been ideal. I didn't because admittedly I could not determine how to.
    guitars = []
    for guitar in item:
        guitar_details = Guitar(guitar[0], guitar[1], guitar[2])
        guitars.append(guitar_details)
    return guitars







main()