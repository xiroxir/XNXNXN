import time
import random
import keyboard as kb
_1 = 0
_11 = 13
_2 = 0
_22 = 2
start = 0
timer = random.randint(5, 10)

counter = 0

def vivod():
    for pipi in spicok:
            for pypy in pipi:
                print(pypy + " ", end='')
            print()
    print()

def padenie():
    global _1, _11, _2, _22
    spicok[_1][_11] = '*'
    spicok[_2][_22] = '*'
    while True:
        
        vivod()
        spicok[_1][_11] = ' '
        _1 = _1+1
        if _1 == 10:
            _1 = 0
        spicok[_1][_11] = '*'
        spicok[_2][_22] = ' '
        _2 = _2 + 1
        if _2 == 9:
            _2 = 0
        spicok[_2][_22] = '*'
        time.sleep(2)
   
spicok = [[' ',' ',' ',' ',' ',' ','/','\\',' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ','/',' ',' ','\\',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ','/',' ',' ',' ',' ','\\',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ','/',' ',' ','\\',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ','/',' ',' ',' ',' ','\\',' ',' ',' ',' '],
          [' ',' ',' ','/',' ',' ',' ',' ',' ',' ','\\',' ',' ',' '],
          [' ',' ',' ',' ',' ','/',' ',' ','\\',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ','/',' ',' ',' ',' ','\\',' ',' ',' ',' '],
          [' ',' ',' ','/',' ',' ',' ',' ',' ',' ','\\',' ',' ',' '],
          [' ',' ','/',' ',' ',' ',' ',' ',' ',' ',' ','\\',' ',' '],
          [' ','/',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\\',' ']]

start = input('Введите начать:')
if start == 'Начать':
    padenie()