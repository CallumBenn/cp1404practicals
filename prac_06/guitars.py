"""
CP1404/CP5632 - Practical 06
Callum Bennett

Emails
Estimate: 45 minutes
Actual: xx minutes
"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    list_of_guitars = []
    list_of_guitars.append(get_guitar())


def get_guitar():
    name = get_valid_string("Name: ")
    year = get_valid_integer("Year: ")
    cost = float(get_valid_float("Cost: "))
    print(f"{name} ({year}) : {cost} added.")
    return name, year, cost



def get_valid_string(instruction):
    """Get and return valid string."""
    try:
        item = input(instruction)
        return item
    except ValueError:
        print("Invalid input!")


def get_valid_integer(instruction):
    """Get and return valid integer."""
    while True:
        try:
            item = int(input(instruction))
            return item
        except ValueError:
            print("Invalid input!")

def get_valid_float(instruction):
    """Get and return valid float."""
    while True:
        try:
            item = float(input(instruction))
            return item
        except ValueError:
            print("Invalid input!")





main()