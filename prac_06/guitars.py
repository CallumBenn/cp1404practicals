"""
CP1404/CP5632 - Practical 06
Callum Bennett

Emails
Estimate: 45 minutes
Actual: 110 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Get and append guitars to list until blank input is entered, then display all guitars"""
    print("My guitars!")
    list_of_guitars = []
    guitar = get_guitar()
    while guitar != "blank":
        list_of_guitars.append(guitar)
        guitar = get_guitar()
    display_guitars(list_of_guitars)


def get_guitar():
    """Get and return guitar name, year and cost"""
    guitars = []
    name = get_valid_string("Name: ")
    if name == "":
        return "blank"
    year = get_valid_integer("Year: ")
    if year == None:
        return "blank"
    cost = get_valid_float("Cost: $")
    if cost == None:
        return "blank"
    guitars += name, year, cost
    print(f"{name} ({year}) : ${cost:.2f} added.")
    return guitars


def display_guitars(guitars):
    """Display string with list values inputted into class"""
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        guitar_details = Guitar(guitar[0], guitar[1], guitar[2])
        vintage_string = "(vintage)" if guitar_details.is_vintage() >= True else ""
        print(f"Guitar {i}: {guitar_details.name:>20} ({guitar_details.year}), worth ${guitar_details.cost:10,.2f} {vintage_string}")


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