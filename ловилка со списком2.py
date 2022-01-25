import time
import random
import keyboard as kb
hp = 3
ochki = 0

def vivod():
    global hp, ochki
    print(hp, ochki)
    for pipi in spicok:
            for pypy in pipi:
                print(pypy + " ", end='')
            print()
    print()
    
def left():
    global yxO
    yxO = -1


def right():
    global yxO
    yxO = 1

kb.add_hotkey('left', left)
kb.add_hotkey('right', right)

def padenie():
    global yxO, hp, ochki
    taimer1 = random.randint(0,5)
    taimer2 = random.randint(0,5)
    taimer3 = random.randint(0,5)
    taimer4 = random.randint(0,5)
    taimer5 = random.randint(0,5)
    taimer6 = random.randint(0,5)
    yO = 9
    xO = 4
    yX1 = -1
    xX1 = 0
    yX2 = -1
    xX2 = 0
    yX3 = -1
    xX3 = 0
    y_bonus1 = -1
    x_bonus1 = 0
    y_bonus2 = -1
    x_bonus2 = 0
    y_bonus3 = -1
    x_bonus3 = 0
    yxO = 0
    
    
    xX1 = random.randint(0,8)
    x_bonus1 = random.randint(0,8)
    while True:
        vivod()
        if taimer1==0:
            spicok[yX1][xX1] = '*'
            yX1 = yX1+1
            if yX1 == yO and xX1 == xO:
                hp = hp-1
            
            if yX1 == 10:
                yX1 = -1
                xX1 = random.randint(0,8)
                taimer1 = random.randint(0,5)
            else:
                spicok[yX1][xX1] = 'X'
        else:
            taimer1 = taimer1 - 1
            spicok[yX1][xX1] = '*'
            
        if taimer2==0:
            spicok[yX2][xX2] = '*'
            yX2 = yX2+1
            if yX2 ==yO and xX2 == xO:
                hp = hp-1
            if yX2 == 10:
                yX2 = -1
                xX2 = random.randint(0,8)
                taimer2 = random.randint(0,5)
            else:
                spicok[yX2][xX2] = 'X'
        else:
            taimer2 = taimer2 - 1
            spicok[yX2][xX2] = '*'
            
        if taimer3==0:
            spicok[yX3][xX3] = '*'
            yX3 = yX3+1
            if yX3 == yO and xX3 == xO:
                hp = hp-1
            if yX3 == 10:
                yX3 = -1
                xX3 = random.randint(0,8)
                taimer3 = random.randint(0,5)
            else:
                spicok[yX3][xX3] = 'X'
        else:
            taimer3 = taimer3 - 1
            spicok[yX3][xX3] = '*'
        
        if taimer4==0:
            spicok[y_bonus1][x_bonus1] = '*'
            y_bonus1 = y_bonus1 + 1
            if y_bonus1== yO and x_bonus1  == xO:
                ochki = ochki + 1
            if y_bonus1 == 10:
                y_bonus1 = -1
                x_bonus1 = random.randint(0,8)
                taimer4 = random.randint(0,5)
            else:
                spicok[y_bonus1][x_bonus1] = '$'
        else:
            taimer4 = taimer4 - 1
            spicok[y_bonus1][x_bonus1] = '*'
        time.sleep(1)
        
        if taimer5==0:
            spicok[y_bonus2][x_bonus2] = '*'
            y_bonus2 = y_bonus2 + 1
            if y_bonus2 == yO and x_bonus2 == xO:
                ochki = ochki + 1
            if y_bonus2 == 10:
                y_bonus2 = -1
                x_bonus2 = random.randint(0,8)
                taimer5 = random.randint(0,5)
            else:
                spicok[y_bonus2][x_bonus2] = '$'
        else:
            taimer5 = taimer5 - 1
            spicok[y_bonus2][x_bonus2] = '*'
        time.sleep(1)
        
        if taimer6==0:
            spicok[y_bonus3][x_bonus3] = '*'
            y_bonus3 = y_bonus3 + 1
            if y_bonus3 == yO and x_bonus3 == xO:
                ochki = ochki + 1
            if y_bonus3 == 10:
                y_bonus3 = -1
                x_bonus3 = random.randint(0,8)
                taimer6 = random.randint(0,5)
            else:
                spicok[y_bonus3][x_bonus3] = '$'
        else:
            taimer6 = taimer6 - 1
            spicok[y_bonus3][x_bonus3] = '*'
        time.sleep(1)
        
        
        if yxO == 1:
            if xO != 8:
                spicok[yO][xO] = '*'
                xO = xO+1
                spicok[yO][xO] = 'O'
                yxO = 0
        elif yxO == -1:
            if xO != 0:
                spicok[yO][xO] = '*'
                xO = xO-1
                spicok[yO][xO] = 'O'
                yxO = 0
        spicok[yO][xO] = 'O'
            
                
   
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