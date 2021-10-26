#!/usr/bin/env python3

#define function that will returns your name and adress
def nameAndAdress(name:str, adress:str):
    """Return on the screen name of user and it\'s adress."""
    print(f'Your name is {name.title()}.\nYour adress is {adress}.')

if __name__ == '__main__':
    #input your name and adress
    name = input('Input here your name, please: ')
    adress = input('Input here your adress, please: ')
    #call function nameAndAdress
    nameAndAdress(name, adress)
