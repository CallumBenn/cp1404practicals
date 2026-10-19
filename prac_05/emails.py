"""
CP1404/CP5632 - Practical 05
Callum Bennett

Emails
Estimate: 40 minutes
Actual: 70 minutes
"""
from typing import Any


def main():
    emails_and_names = {}
    email = input("Email: ")
    emails_and_names[email] = determine_name(email)

    choice = input(f"Is your name {emails_and_names[email]}? (Y/n) ").upper()
    while choice == "Y" or choice == "":
        email = input("Email: ")
        emails_and_names[email] = determine_name(email)
        choice = input(f"Is your name {emails_and_names[email]}? (Y/n) ").upper()

    name = input("Name: ")
    if name != "":
        emails_and_names[email] = determine_name(name)
    email = input("Email: ")
    if email != "":
        emails_and_names[email] = determine_name(name)
    print_emails(emails_and_names)


def determine_name(item):
    name = " ".join(item.split("@", 1)[0].split(".")).title()
    return name


def print_emails(emails):
    for i in emails:
        print(f"{emails[i]} ({i})")



main()