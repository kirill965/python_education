#!/usr/bin/env python3

"""Calculating cylinder volume"""
#import PI value from math module
from math import pi as PI

#input radius and height from user
radius, height = [float(item) for item in input('Enter here radius and height, through comma: ').split(', ')]

#calculations
cylinderVolume = (PI * (radius ** 2)) * height

#print result on the screen
print('Volume of cylinder with radius %0.2f and height %0.2f is %0.2f' % (radius, height, cylinderVolume))
