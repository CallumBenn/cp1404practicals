"""
CP1404/CP5632 - Practical 06
Callum Bennett

Emails
Estimate: 45 minutes
Actual: xx minutes
"""

from prac_06.guitar import Guitar


guitars = [["Gibson L-5 CES",1922,16035.40], ["Another Guitar", 2017, 100.00]]
for guitar in guitars:  # Compare age determined by program and class
    guitar_information = Guitar(guitar[0],guitar[1], guitar[2])
    print(f"{guitar[0]} get_age() - Expected {2026 - guitar[1]}. Got {guitar_information.get_age()}")
for guitar in guitars:  # Compare vintage status determined by program and class
    guitar_information = Guitar(guitar[0], guitar[1], guitar[2])
    is_vintage = False
    if (2026 - guitar[1]) > 50:
        is_vintage = True
    print(f"{guitar[0]} is_vintage() - Expected {is_vintage}. Got {guitar_information.is_vintage()}")
