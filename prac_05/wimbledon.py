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
times_won = {}

with open(filename, "r", encoding="utf-8-sig") as in_file:
    # file = csv.reader(in_file)
    in_file.readline()
    for line in in_file:
        parts = line.split(',')
        champions.append(parts[2])
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
print(times_won)
    # champions_and_scores =
