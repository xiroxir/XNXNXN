import pyautogui
import time
pyautogui.hotkey('win', 'r')
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write('Zubnoj v 8:00')
pyautogui.hotkey('ctrl', 's')
time.sleep(0.5)
pyautogui.write('Zubnoj')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('left')
pyautogui.press('enter')

