import pyautogui as py
import time
n = int(input('Введите число:'))
for step in range(1,n+1):
    py.hotkey('win', 'r')
    time.sleep(0.2)
    py.write('notepad')
    time.sleep(0.2)
    py.press('enter')
    py.hotkey('ctrl', 's')
    time.sleep(0.2)
    py.moveTo(345, 319)
    time.sleep(0.2)
    py.click()
    time.sleep(0.2)
    py.moveTo(475,345)
    time.sleep(0.2)
    py.doubleClick()
    time.sleep(0.2)
    py.moveTo(488,260)
    time.sleep(0.2)
    py.doubleClick()
    time.sleep(0.2)
    py.moveTo(400,497)
    time.sleep(0.2)
    py.click()
    time.sleep(0.2)
    py.write(str(step))
    time.sleep(0.2)
    py.press('enter')
    time.sleep(0.2)
    py.press('enter')
