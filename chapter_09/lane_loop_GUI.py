""" lane_loop_GUI.py - check lane is safe and count total crash

Author: Harry
Date: 2026-11-25
"""

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="#333333")
canvas.pack()

# 用迴圈畫車道線：lane 走 1, 2, 3 -> 畫 3 條線
for lane in range(1, 5):
    x = lane * 100
    canvas.create_line(x, 0, x, 500, fill="white", dash=(10, 10))

# 用迴圈畫一排紅車：每個車道中間放一台
for lane in range(0, 5):
    cx = lane * 100 + 50
    canvas.create_rectangle(cx - 20, 420, cx + 20, 480, fill="red")

root.mainloop()