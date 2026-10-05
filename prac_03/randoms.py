"""
CP1404/CP5632 - Practical 03
Callum Bennett
"""
# What did you see on line 1?
# Answer: 8
# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest was 5, largest was 20

# What did you see on line 2?
# Answer: 5
# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest was 3, largest was 9
# Could line 2 have produced a 4?
# Answer: No. Because the code is instructed to step over every second number, and the number range starts at 3, all even numbers are skipped

# What did you see on line 3?
# Answer: 4.365456331836537
# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest was 2.5, largest was 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
# Answer:
import random

print(random.randint(1, 100))