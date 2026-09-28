"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random
RANDOM_NUMBER = random.randint(1, 100)

def main():
    """Get score, reject invalid score, print score status and print random number with relative status"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        score = float(input("Invalid score \nEnter score: "))
    print(f"{score} is {determine_status(score)}")
    if determine_status(score) == "Excellent":
        print("You get a prize!")
    print(f"Random: {RANDOM_NUMBER} = {determine_status(RANDOM_NUMBER)}")


def determine_status(score):
    """Determine score status based on score"""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()

