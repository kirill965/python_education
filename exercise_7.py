#!/usr/bin/env python3

#import math module
import math

#input height in meters from user
height = float(input('Enter the height from which the object will fall in meters: '))

#acceleration of gravity
accOfGrav = 9.8

#calculations
speed = math.sqrt(2 * accOfGrav * height)

#output result on the screen
print('Body velocity at the moment of impact from a height is %.2fm' % speed)
