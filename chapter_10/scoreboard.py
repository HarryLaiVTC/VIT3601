""" scoreboard.py - list of dicts + set + json to store scoreboard

Author: Harry
Date: 2026-11-25
"""

import json

screen_size = (500, 500)
print("Screen size: " + str(screen_size))

high_scores = [
    {"name": "Ann", "score": 5},
    {"name": "Bob", "score": 9},
    {"name": "Ann", "score": 7},
]

for entry in high_scores:
    print(entry["name"] + ": " + str(entry["score"]))

print("Top name: " + high_scores[0]["name"])

names = set()
for entry in high_scores:
    names.add(entry["name"])
print("Distinct players: " + str(len(names)))

print(json.dumps(high_scores))