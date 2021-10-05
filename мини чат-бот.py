import pyautogui as py
import time
a=input('Введите запрос:')
if a=='Выход':
    py.hotkey('alt', 'f4')
    py.press('enter')
elif a == 'Текст':
    py.hotkey('win', 'r')
    py.write('notepad')
    py.press('enter')
elif a == 'Поиск':
    zapros = input('Введите запрос (На английском):')
    py.hotkey('ctrl', 'alt', 'g')
    time.sleep(1)
    py.write(zapros)
    py.press('enter')
else:
    print('Я такой команды не знаю...')
        
