"""Get password made of # characters or more and print number of stars matching length of password"""


# pseudocode:
# get password
# while password length less than 8
#     print error message
#     get password
# print star symbol x password length


MINIMUM_LENGTH = 8

def main():
    """Get password then print stars"""
    password = get_password()
    print_stars(password)


def get_password() -> str:
    """Get password from user and reject password if length under MINIMUM_LENGTH"""
    password = input("Enter password: ")
    while len(password) < 8:
        password = input(f"Password must be at least {MINIMUM_LENGTH} characters!\nEnter password: ")
    return password


def print_stars(password: str):
    """Print stars numbering the same length of password"""
    print("*" * len(password), sep='')


main()