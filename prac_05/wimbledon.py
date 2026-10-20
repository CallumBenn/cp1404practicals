"""
CP1404/CP5632 - Practical 05
Callum Bennett

Wimbledon
Estimate: 50 minutes
Actual: xx minutes
"""
from cmath import exp

# import csv

filename = "wimbledon.csv"
champions = []
winning_countries = {}
times_won = {}



with open(filename, "r", encoding="utf-8-sig") as in_file:
    # file = csv.reader(in_file)
    in_file.readline()
    for line in in_file:
        parts = line.split(',')
        champions.append(parts[2])
        winning_countries[parts[3]] = parts[3]
        # print(parts[2])
# print(champions)


try:
    for name in champions:
        # print(name)
        if name not in times_won:
            times_won[name] = 0
        times_won[name] += 1
except KeyError:
    print("Invalid name")


print("Wimbledon Champions:")
for name in times_won:
    print(name, times_won[name])

number_of_countries = 0
for country in winning_countries:
    number_of_countries += 1
print(f"\nThese {number_of_countries} countries have won Wimbledon:")
# for country in winning_countries:
#     print(", ".join(country.strip(",")))
print(", ".join(winning_countries))