#!/usr/bin/env python3

"""Calculation of area and volume with given radius."""
#from math module import pi value
from math import pi as PI

#input radius from user
r = float(input('Enter here a value of the radius in centimeters: '))
#calculations
area = round(PI * (r ** 2), 2)
volume = round((4 * PI * (r ** 3)) / 3, 2)

#print result on the screen
print(f'Area of a circle with radius {int(r)} is {area}\nSphere volume with radius {int(r)} is {volume}')
