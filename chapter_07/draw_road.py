""" draw_road.py - Draw road in GUI.

Author: Harry
Date: 2026-11-25
"""

import tkinter as tk

WIDTH = 300
HEIGHT = 500

root = tk.Tk()
root.title("Car Dodge - Lesson 1: Draw the Road")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#333333")
canvas.pack()

# two dashed lane lines (vertical) at x = 100 and x = 200
canvas.create_line(100, 0, 100, HEIGHT, fill="white", dash=(10, 10))
canvas.create_line(200, 0, 200, HEIGHT, fill="white", dash=(10, 10))

# player car (cyan) centred in the middle lane at the bottom
canvas.create_rectangle(130, 420, 170, 480, fill="cyan")

# obstacle car (red) centred in the left lane near the top
canvas.create_rectangle(30, 40, 70, 100, fill="red")

root.mainloop()