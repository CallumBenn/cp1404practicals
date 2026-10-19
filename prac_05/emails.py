"""
CP1404/CP5632 - Practical 05
Callum Bennett

Emails
Estimate: 30 minutes
Actual: xx minutes
"""

# ALPHANUMERIC_CHARACTERS = "abcdefghijklmnopoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

emails_and_names = {}
# name = []
# email = input("Email: ")
email = "lindsay.ward@jcu.edu.au"
# unformatted_name = email.split("@", 1)[0].split(".")
# name = email.split("@", 1)[0].split(".")
name = " ".join(email.split("@", 1)[0].split(".")).title()
# for character in unformatted_name:
#     if character not in ALPHANUMERIC_CHARACTERS:
#         character = " "
#     name += character
print(name)                 # DELETE THIS
emails_and_names[email] = name

choice = input(f"Is your name {name}? (Y/n)").upper()
while choice != "Y":
    email = input("Email: ")
    name = email.split("@", 1)[0].split(".")
    choice = input(f"Is your name {name}? (Y/n)").upper()
    emails_and_names[email] = name

for i in emails_and_names:
    print(emails_and_names[i], i)



