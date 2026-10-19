"""
CP1404/CP5632 - Practical 05
Callum Bennett

Word Occurences
Estimate: 30 minutes
Actual: xx minutes
"""
from shlex import split


text = "This is a test. test This is a. Test Is A."
words_to_count = {}

for word in text.split():
    try:
        words_to_count[word] += 1
    except KeyError:
        words_to_count[word] = 1
print(words_to_count)




# print(text)
# for character in text:
#     try:
#         word = character.split(" ")
#         characters_to_count[character] += 1
#     except KeyError:
#         characters_to_count[character] = 1
# print(characters_to_count)
# for character in sorted(characters_to_count):
#     print(character, characters_to_count[character])