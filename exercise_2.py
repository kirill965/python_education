#!/usr/bin/env python3

"""Program that greets user."""

def greetUser(name:str):
    """Return on the screen greeting with name of the user."""
    print(f'Hello {name.title()}! Nice to meet you.')

if __name__ == '__main__':
    name = input('Enter your name here: ')
    greetUser(name)

