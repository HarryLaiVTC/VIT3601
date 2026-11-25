""" lane_loop.py - check lane is safe and count total crash

Author: Harry
Date: 2026-11-25
"""

player_lane = int(input("Player lane (0, 1 or 2): "))
obstacle_lanes = [0, 2, 1, 2]

crashes = 0
for i in range(len(obstacle_lanes)):
    lane = obstacle_lanes[i]
    if lane == player_lane:
        print("CRASH in lane " + str(lane) + "!")
        crashes = crashes + 1
    else:
        print("Safe in lane " + str(lane) + ".")

print("Total crashes: " + str(crashes))