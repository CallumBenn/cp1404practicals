"""
CP1404/CP5632 - Practical 03
Callum Bennett
"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# use f-string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,036!
print(f"{year} {name} for about ${cost:,.0f}")

# produce the following right-aligned output (DO NOT use a list):
# 2 ^ 0 is    1
# 2 ^ 1 is    2
# 2 ^ 2 is    4
# 2 ^ 3 is    8
# 2 ^ 4 is   16
# 2 ^ 5 is   32
# 2 ^ 6 is   64
# 2 ^ 7 is  128
# 2 ^ 8 is  256
# 2 ^ 9 is  512
# 2 ^10 is 1024
for i in range(0, 11):
    print(f"2 ^ {i} is {2 ** i:4}")