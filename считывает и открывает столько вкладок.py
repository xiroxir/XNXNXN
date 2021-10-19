import pyautogui as py
n = int(input('Введите число от 1 до 9:'))
py.hotkey('ctrl', 'alt', 'g')
for step in range(1, n+1):
    py.hotkey('ctrl', 't')
