"""
CP1404/CP5632 - Practical 05
Callum Bennett

Wimbledon
Estimate: 50 minutes
Actual: 80 minutes
"""
from cmath import exp

filename = "wimbledon.csv"
champions = []
winning_countries = {}


def main():
    """Import, and assign data from, file then execute rest of program"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.split(',')
            champions.append(parts[2])
            winning_countries[parts[3]] = parts[3]
    champion_wins = count_wins(champions)
    print_champions(champion_wins)
    print("")
    print_winning_countries(winning_countries)


def count_wins(names):
    """Count each champion's wins into dictionary"""
    wins = {}
    for name in names:
        if name not in wins:
            wins[name] = 0
        wins[name] += 1
    return wins


def print_champions(wins):
    """Print each champion name and number of wins"""
    print("Wimbledon Champions:")
    for name in wins:
        print(name, wins[name])


def print_winning_countries(countries):
    """Print number of countries then each country"""
    number_of_countries = 0
    for country in countries:
        number_of_countries += 1
    print(f"These {number_of_countries} countries have won Wimbledon:")
    print(", ".join(countries))


main()
