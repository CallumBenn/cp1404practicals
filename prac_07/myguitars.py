"""
CP1404/CP5632 - Practical 07
Callum Bennett

Estimate: 35 minutes
Actual: 30 minutes
"""


from guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""
    in_file = open('guitars.csv', 'r')
    guitars = get_guitars(in_file)
    for guitar in guitars:
        print(guitar)
    in_file.close()

def get_guitars(file):
    guitars = []
    for line in file:
        parts = line.strip().split(',')
        parts[1] = int(parts[1])
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
    guitars.sort()
    return guitars


main()