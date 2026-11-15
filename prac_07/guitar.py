"""
CP1404/CP5632 - Practical 07
Callum Bennett
"""

import datetime


VINTAGE_AGE = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return current year minus guitar year."""
        return datetime.datetime.now().year - self.year

    def is_vintage(self):
        """Return True if guitar age is greater than VINTAGE_AGE."""
        if Guitar.get_age(self) > VINTAGE_AGE:
            return True
        else:
            return False

    def __lt__(self, other):
        """Return True if self.year is less than other.year"""
        return self.year < other.year

    def __str__(self):
        """Return guitar name and year within string"""
        return f"My guitar: {self.name}, first made in {self.year}"
