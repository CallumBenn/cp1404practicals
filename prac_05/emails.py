"""
CP1404/CP5632 - Practical 05
Callum Bennett

Emails
Estimate: 40 minutes
Actual: 80 minutes
"""
from typing import Any


def main():
    """Get and store names and email addresses in dictionary, then print contents of dictionary"""
    email_to_name = {}
    email = input("Email: ")
    email_to_name[email] = remove_symbols(email)

    choice = input(f"Is your name {email_to_name[email]}? (Y/n) ").upper()
    while choice == "Y" or choice == "":
        email = input("Email: ")
        email_to_name[email] = remove_symbols(email)
        choice = input(f"Is your name {email_to_name[email]}? (Y/n) ").upper()

    name = input("Name: ")
    if name != "":
        email_to_name[email] = remove_symbols(name)
    email = input("Email: ")
    if email != "":
        email_to_name[email] = remove_symbols(name)
    print_items(email_to_name)


def remove_symbols(string):
    """Remove '@' and '.' from string"""
    name = " ".join(string.split("@", 1)[0].split(".")).title()
    return name


def print_items(items):
    """Print each key and its item in a dictionary"""
    for i in items:
        print(f"{items[i]} ({i})")


main()
