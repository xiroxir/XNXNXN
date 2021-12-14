import time
import random
import keyboard as kb
yX = 0
xX = 0
y_bonus = 0
x_bonus = 0
num1 = 0
start = 0

def vivod():
    for pipi in spicok:
            for pypy in pipi:
                print(pypy + " ", end='')
            print()
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
          ['*','*','*','*','O','*','*','*','*']]

start = input('Введите начать:')
if start == 'Начать':
    xX = random.randint(0,9)
    while start != 'Выход':
        spicok[yX][xX] = 'X'
        vivod()
        spicok[yX][xX] = '*'
        yX = yX+1
        if yX == 10:
            yX = 0
            xX = random.randint(0,9)
        time.sleep(2)