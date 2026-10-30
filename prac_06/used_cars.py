"""
CP1404/CP5632 - Practical 06
Callum Bennett
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(Car.__str__(limo))
    print(limo)


main()
