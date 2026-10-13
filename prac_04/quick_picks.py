"""
CP1404/CP5632 - Practical 04
Callum Bennett
"""
import random

NUMBER_RANGES=  [1, 45]
LINE_LENGTH = 6

previous_random_number = []

number_of_lines = int(input("How many quick picks? "))
for line in range(number_of_lines):
    for number in range(LINE_LENGTH):
        random_number = random.randint(NUMBER_RANGES[0], NUMBER_RANGES[1])
        while random_number in previous_random_number:  # check list for repeat numbers
            random_number = random.randint(NUMBER_RANGES[0], NUMBER_RANGES[1])
        previous_random_number.append(random_number)    # add current random number to list
        print(f"{random_number:2}", end=" ")
    print("")   # insert line break to match example output formatting
