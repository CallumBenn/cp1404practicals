"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
for state_code in STATE_NAMES:
    print(f"{state_code:3} is {STATE_NAMES[state_code]}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in STATE_NAMES:
        print(state_code, "is", STATE_NAMES[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()