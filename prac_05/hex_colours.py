"""
CP1404/CP5632 - Practical 05
Callum Bennett
"""
from idlelib.autocomplete_w import KEYRELEASE_SEQUENCE

COLOUR_CODES = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "AliceBlue": "#f0f8ff", "AlizarinCrimson": "#e32636",
                "AntiqueWhite": "#faebd7", "ArmyGreen": "#4b5320", "ArylideYellow": "#e9d66b", "BabyPink": "#f4c2c2",
                "BananaMania": "#fae7b5", "CadmiumRed": "#e30022"}

colour = input("Enter a colour: ")
while colour != "":
    try:
        print(COLOUR_CODES[colour])
    except KeyError:
        print("Colour not found!")
    colour = input("Enter a colour: ")