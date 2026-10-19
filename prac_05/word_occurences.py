"""
CP1404/CP5632 - Practical 05
Callum Bennett

Word Occurences
Estimate: 30 minutes
Actual: 52 minutes
"""
from shlex import split

text = input("Text: ")
words_to_count = {}
longest_length = 0

for word in text.split():
    try:
        words_to_count[word] += 1
    except KeyError:
        words_to_count[word] = 1

for word in words_to_count.keys():
    if len(word) > longest_length:
        longest_length = len(word)

for word in sorted(words_to_count):
    print(f"{word:{longest_length}} : {words_to_count[word]}")





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