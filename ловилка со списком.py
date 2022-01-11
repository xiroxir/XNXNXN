import time
import random
import keyboard as kb
yX = -1
xX = 0
y_bonus = -1
x_bonus = 0
num1 = 0
start = 0
XorD = 0
otchet = 0
taimer = random.randint(1,5)
taimer2 = random.randint(1,5)

def vivod():
    for pipi in spicok:
            for pypy in pipi:
                print(pypy + " ", end='')
            print()
    print()

def padenie():
    global XorD, yX, xX, y_bonus, x_bonus, taimer, taimer2ы
    XorD = random.randint(0,1)
    xX = random.randint(0,8)
    x_bonus = random.randint(0,8)
    while True:
        vivod()
        if taimer==0:
            spicok[yX][xX] = '*'
            yX = yX+1
            if yX == 10:
                yX = -1
                xX = random.randint(0,8)
                taimer = random.randint(1,5)
            else:
                spicok[yX][xX] = 'X'
        else:
            taimer = taimer - 1
            spicok[yX][xX] = '*'
        
        if taimer2==0:
            spicok[y_bonus][x_bonus] = '*'
            y_bonus = y_bonus + 1
            if y_bonus == 10:
                y_bonus = -1
                x_bonus = random.randint(0,8)
                taimer2 = random.randint(1,5)
            else:
                spicok[y_bonus][x_bonus] = '$'
        else:
            taimer2 = taimer2 - 1
            spicok[y_bonus][x_bonus] = '*'
        time.sleep(1)
   
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
    padenie()