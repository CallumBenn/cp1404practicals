"""
CP1404/CP5632 - Practical 03
Callum Bennett
"""
from _pyrepl import readline

# 1
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", 'r')
print(f"Hi {in_file.readline()}!")
in_file.close()

# 3
in_file = open("numbers.txt", 'r')
print(int(in_file.readline()) + int(in_file.readline()))    # each 'readline()' reads the next sequential line in file
in_file.close()

# 4
total = 0
with open("numbers.txt", 'r') as file:
    for line in file:
        total += int(line)
print(total)

