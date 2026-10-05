"""
CP1404/CP5632 - Practical 03
Callum Bennett
"""

# 1. When will a ValueError occur?
# Answer: When an alphabetical character or float is entered

# 2. When will a ZeroDivisionError occur?
# Answer: When Python attempts to divide by zero

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Answer: A 'while' loop could check if either numerator or denominator are set to '0' and request re-input

def main():
    """Calculate numerator divided by denominator"""
    try:
        numerator = get_valid_number("Enter the numerator: ")
        denominator = get_valid_number("Enter the denominator: ")
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")

def get_valid_number(message):
    """Get and return integer which is not '0'"""
    number = int(input(message))
    while number == 0:
        number = int(input(f"Cannot divide by zero!"
                           f"\n{message}"))
    return number

main()