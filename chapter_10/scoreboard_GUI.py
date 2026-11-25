""" scoreboard_GUI.py - list of dicts + set + json to store scoreboard

Author: Harry
Date: 2026-11-25
"""
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="#333333")
canvas.pack()

# 每台車是一個 dict：x 位置 + color 顏色
cars = [
    {"x": 50, "color": "red"},
    {"x": 150, "color": "yellow"},
    {"x": 250, "color": "lime"},
    {"x": 350, "color": "cyan"},
    {"x": 450, "color": "magenta"},
]

# 用 for 逐個取出 dict，畫在各自的 x 上
for car in cars:
    canvas.create_rectangle(car["x"] - 20, 420, car["x"] + 20, 480, fill=car["color"])

root.mainloop()