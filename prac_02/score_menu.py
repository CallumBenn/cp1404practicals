"""Get score, print result and show stars"""


# pseudocode:
# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message


MENU_CHOICES = "(G)et a valid score \n(P)rint result \n(S)how stars \n(Q)uit \n>>> "

def main():
    score = 0   # Set default score
    choice = input(MENU_CHOICES).upper()
    while choice != "Q":
        print("")   # Insert line break for formatting
        if choice == "G":
            score = int(get_score())
        elif choice == "P":
            print(f"Score: {score} - {determine_status(score)}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print("")   # Insert line break for formatting
        choice = input(MENU_CHOICES).upper()
    print("Finished.")


def get_score():
    """Get valid score"""
    user_score = float(input("Enter score: "))
    while user_score < 0 or user_score > 100:
        user_score = float(input("Invalid score \nEnter score: "))
    return user_score


def determine_status(number):
    """Determine score status based on score"""
    if number < 50:
        return "Bad"
    elif number < 90:
        return "Passable"
    else:
        return "Excellent"


def print_stars(number):
    """Print stars numbering the same length of password"""
    print("*" * int(number), sep='')


main()