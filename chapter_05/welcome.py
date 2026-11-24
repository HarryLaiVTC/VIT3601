""" welcome.py - calculate age next year.

Author: Harry
Date: 2026-11-24
"""

import random
def greet(name):
    print("Hello, " + name + "!")
name = input("Your name: ")
greet(name)
greet("VIT3601")
print("Lucky number: %d" % random.randint(1, 10))

