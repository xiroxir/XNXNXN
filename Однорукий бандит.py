import random
import keyboard as kb
import pyautogui as py
import time
comand = input("Введите команду:")
num1 = int(0)
num2 = int(0)
num3 = int(0)
genius = int(0)
ochki = int(0)
def proverka():
    global ochki,comand
    if comand == 'Однорукий бандит':
        py.press('backspace')
        if num1==num2 and num1==num3:
            ochki = ochki + 1
            print('Молодец ты получил одно очко')
        else:
            ochki = ochki - 1
            print('Ошибка, -одно очко')
def podchet():
    global genius, ochki, comand
    py.press('backspace')
    comand = 0
    time.sleep(0.5)
    print(ochki)
    ochki = 0
    
kb.add_hotkey('space',proverka)
kb.add_hotkey('z', podchet)
while comand != 'Exit':
    while comand == 'Однорукий бандит':
        num1 = random.randint(1, 3)
        num2 = random.randint(1, 3)
        num3 = random.randint(1, 3)
        print(num1, num2, num3)
        time.sleep(1)
    comand = input("Введите команду:")