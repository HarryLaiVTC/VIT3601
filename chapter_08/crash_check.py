""" crash_check.py - if else logic, check crash.

Author: Harry
Date: 2026-11-25
"""

player_lane = int(input("Player lane (0, 1 or 2): "))
obstacle_lane = int(input("Obstacle lane (0, 1 or 2): "))

if player_lane == 0 and obstacle_lane == 0:
    print("CRASH in the left lane!")
elif player_lane == 1 and obstacle_lane == 1:
    print("CRASH in the middle lane!")
elif player_lane == 2 and obstacle_lane == 2:
    print("CRASH in the right lane!")
else:
    print("Safe. Different lanes.")

    