import pyautogui as pg
import pyperclip
import time
num1 = input('Введите любой текст:')
pyperclip.copy(num1)
pg.hotkey('ctrl', 'alt', 'g')
time.sleep(1)
pg.hotkey('ctrl', 'v')
pg.press('enter')
