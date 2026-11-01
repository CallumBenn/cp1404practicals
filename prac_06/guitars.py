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

    guitar = get_guitar()
    while guitar != "blank":
        list_of_guitars.append(guitar)
        guitar = get_guitar()


def get_guitar():
    guitars = []
    name = get_valid_string("Name: ")
    if name == "":
        return "blank"
    year = get_valid_integer("Year: ")
    if year == None:
        return "blank"
    cost = get_valid_float("Cost: ")
    if cost == None:
        return "blank"
    guitars += name, year, cost
    return guitars








def get_valid_string(instruction):
    """Get and return valid string."""
    item = input(instruction)
    return item


def get_valid_integer(instruction):
    """Get and return valid integer."""
    while True:
        try:
            item = int(input(instruction))
            return item
        except ValueError:
            return None


def get_valid_float(instruction):
    """Get and return valid float."""
    while True:
        try:
            item = float(input(instruction))
            return item
        except ValueError:
            return None





main()