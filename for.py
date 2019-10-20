#!/usr/bin/env python3

# For loop

colors = ['blue', 'red', 'orange', 'purple']

for color in colors:
    print(color)

for color in colors:
    if color == 'blue':
        continue
    elif color == 'purple':
        break
    print(color)

point = (2.1, 3.0, 7)
for value in point:
    print(value)

ages = {'Robert': 48, 'Vida': 40, 'Gabe': 14, 'Angelica': 10}
for key in ages:
    print(f"{key} is {ages[key]}")

for letter in "my_string":
    print(letter)

list_of_points = [(2, 3), (1,2), (4,5), (7, 8)]
for x, y in list_of_points:
    print(f"x: {x}, y: {y}")

for name, age in ages.items():
    print(f"Person is named: {name}")
    print(f"Age of {age}")
