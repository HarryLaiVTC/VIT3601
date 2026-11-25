""" average.py - calculate average of 2 numbers.

Author: Harry
Date: 2026-11-24
"""

a = float(input("Score 1: "))
b = float(input("Score 2: "))
avg = (a + b) / 2
print("Average is %f" % avg)
print("Pass?", avg > 50)
