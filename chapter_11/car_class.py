""" car_class.py - class Car

Author: Harry
Date: 2026-11-25
"""

class Car:
    def __init__(self, x, color):          # (1) 補回行尾的冒號 :
        self.x = x
        self.color = color

    def move(self):
        self.x = self.x + 10               # (2) x 前面補 self.

    def describe(self):
        return self.color + " car at x=" + str(self.x)


red_car = Car(50, "red")
blue_car = Car(200, "blue")

print(red_car.describe())
red_car.move()
print("red_car.x = " + str(red_car.x))    # (3) speed 沒有這個屬性，應是 red_car.x
print(red_car.describe())
print(blue_car.describe())

