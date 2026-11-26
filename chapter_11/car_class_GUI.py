""" car_class_GUI.py - class Car

Author: Harry
Date: 2026-11-25
"""

import tkinter as tk

class Car:
    def __init__(self, x, color):
        self.x = x
        self.color = color
        self.y = 420
        self.item = None

    def draw(self, canvas):
        self.canvas = canvas
        self.item = canvas.create_rectangle(self.x - 20, self.y, self.x + 20, self.y + 60, fill=self.color)

    def move(self):
        self.y = self.y + 10
        self.canvas.move(self.item, 0, 10)

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="#333333")
canvas.pack()

cars = [Car(50, "red"), Car(150, "yellow"), Car(250, "lime"), Car(350, "cyan")]

for car in cars:
    car.draw(canvas)

# 範例：叫第一台車往下移 10（move 改的是 self.y），再重畫一次
cars[0].move()

root.mainloop()