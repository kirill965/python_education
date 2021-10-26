#!/usr/bin/env python3
"""Программа расчитывающая количество денег, которое будет на счету в банке, с заранее определенным процентом, по годам."""

def percentBank():
    start_ = float(input('Введите сумму первоначального взноса здесь: '))
    years_ = int(input('Введите количество лет, для вашего депозита: '))
    PERCENT = 1.04
    resultList = [round((start_ * (PERCENT ** (i+1))),2) for i in range(years_)]
    counter = 0
    for item in resultList:
        counter += 1
        print(f'Год: {counter} Выплата: {item}')
if __name__ == '__main__':
    percentBank()
