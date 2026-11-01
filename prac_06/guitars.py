"""
CP1404/CP5632 - Practical 06
Callum Bennett

Emails
Estimate: 45 minutes
Actual: xx minutes
"""

from prac_06.guitar import Guitar

GUITAR_PROMPTS = ["Name: ", "Year: ", "Cost: "]

def main():
    print("My guitars!")
    list_of_guitars = []

    get_guitar()
    while get_guitar() != "blank":
        get_guitar()
    # GET A NUMBER OF INPUTS AND STORE EACH ONE IN LIST, THEN TAKE THE 2ND AND 3RD INPUTS AND MAKE THEM INT AND FLOAT RESPECTIVELY

def get_guitar():
    prompt_index = -1
    guitars = []
    guitar = ""
    # while guitar != "":
    for prompt in range(0, len(GUITAR_PROMPTS)):
        print(len(GUITAR_PROMPTS))
        prompt_index += 1
        guitar.append(get_valid_string(GUITAR_PROMPTS[prompt_index]).split(","))
        if guitar == "":
            return "blank"
        guitars.append(guitar)
    return guitars








def get_valid_string(instruction):
    """Get and return valid string."""
    item = input(instruction)
    return item


# def get_valid_integer(instruction):
#     """Get and return valid integer."""
#     while True:
#         try:
#             item = int(input(instruction))
#             return item
#         except ValueError:
#             print("Invalid input!")
#
# def get_valid_float(instruction):
#     """Get and return valid float."""
#     while True:
#         try:
#             item = float(input(instruction))
#             return item
#         except ValueError:
#             print("Invalid input!")





main()