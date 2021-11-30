import time
import random
import keyboard as kb
yO = 0
xO = 0
y_bonus = 0
x_bonus = 0
num1 = 0

def bomba():
    global xO, yO
    global spicok
    xO = random.randint(0,9)
    spicok[yO][xO] = 'O'

def bonus():
    global x_bonus, y_bonus
    global spicok
    x_bonus = random.randint(0,9)
    spicok[y_bonus][x_bonus] = '$'

def special():
    global num1
    global spicok
    num1 = random.randint(1,2)
    if num1 == 1:
        bomba()
    elif num1 == 2:
        bonus()
    for pipi in spicok:
        for pypy in pipi:
            print(pypy + " ", end='')
        print() 

spicok = [['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','K','*','*','*','*']]

special()