"""
CP1404/CP5632 - Practical 06
Callum Bennett

Emails
Estimate: 30 minutes
Actual: 22 minutes
"""

from prac_06.languages import ProgrammingLanguage


python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
             ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
             ProgrammingLanguage("Visual Basic", "Static", False, 1991)]
print("The dynamically typed languages are:")
for i in languages:
    if i.reflection:
        print(i.language)