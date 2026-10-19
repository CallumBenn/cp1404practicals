"""
CP1404/CP5632 - Practical 05
Callum Bennett

Word Occurences
Estimate: 30 minutes
Actual: xx minutes
"""
from shlex import split

characters_to_count = {}
text = "This is a test"
for character in text:
    try:
        characters_to_count[character] += 1
    except KeyError:
        characters_to_count[character] = 1
print(characters_to_count)
for character in characters_to_count:
    print(character, characters_to_count[character])