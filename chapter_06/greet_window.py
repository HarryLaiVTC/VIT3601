""" greet_window.py - greeting tkinter GUI.

Author: Harry
Date: 2026-11-25
"""
import tkinter

course = "VIT3601"

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=300, height=120)
canvas.pack()
msg = canvas.create_text(150, 60, text="")

tkinter.Label(window, text="Your name:").pack()
entry = tkinter.Entry(window)
entry.pack()

def greet():
    name = entry.get()
    canvas.itemconfig(msg, text=name + ", you are in " + course + " this year.")

tkinter.Button(window, text="Greet", command=greet).pack()
window.mainloop()
