#!/usr/bin/env python3
"""Converting feet and inches to centimeters"""
feet = int(input('Введите количество фунтов в вашем росте: '))
inches = int(input('Введите количество дюймов в вашем росте: '))

centimeters = (inches + feet * 12) * 2.54

print(f'Ваш рост: {round(centimeters,2)}см.')
