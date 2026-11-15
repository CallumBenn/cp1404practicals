"""
CP1404/CP5632 - Practical 07
Callum Bennett

Estimate: 35 minutes
Actual: 30 minutes
"""

from typing import Any
from guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""
    in_file = open('guitars.csv', 'r')
    guitars = format_from_csv(in_file)

    new_guitars = get_guitar()
    guitars = append_to_guitars(guitars, new_guitars)
    in_file.close()
    display_list(guitars)


def append_to_guitars(guitars, new_guitars):
    """Append new guitars to list of guitars, then sort list."""
    for guitar in new_guitars:
        guitars.append(guitar)
    guitars.sort()
    return guitars



def display_list(item):
    """Print items in list."""
    for guitar in item:
        print(guitar)


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
        guitars = format_from_list(guitars)
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