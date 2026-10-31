"""
CP1404/CP5632 - Practical 06
Callum Bennett

Emails
Estimate: 30 minutes
Actual: 22 minutes
"""


class ProgrammingLanguage:
    def __init__(self, language, typing="", reflection=False, year=0):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True/False if the programming language is dynamically typed or not."""
        if self.typing == "Dynamic":
            return self.reflection == True
        else:
            return None

    def __str__(self):
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
