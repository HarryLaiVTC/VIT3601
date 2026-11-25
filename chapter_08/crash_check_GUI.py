""" crash_check_GUI.py - if else logic, check crash.

Author: Harry
Date: 2026-11-25
"""

import tkinter as tk

player_lane = 0
obstacle_lane = 0

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=500, bg="#333333")
canvas.pack()

def lane_x(lane):
    return lane * 100 + 50

# obstacle car (red) near the top
canvas.create_rectangle(lane_x(obstacle_lane) - 20, 40, lane_x(obstacle_lane) + 20, 100, fill="red")

if player_lane == obstacle_lane:
    car_color = "red"
    msg = "CRASH!"
else:
    car_color = "cyan"
    msg = "Safe"
canvas.create_rectangle(lane_x(player_lane) - 20, 420, lane_x(player_lane) + 20, 480, fill=car_color)
canvas.create_text(150, 250, text=msg, fill="white", font=("Arial", 24, "bold"))
root.mainloop()





    