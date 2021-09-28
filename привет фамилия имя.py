import pyautogui as pg
imya = input('Введите имя:')
familia = input('Введите фамилию:')
pg.alert(text= 'Привет '+ imya +' '+familia, title='Привет '+ imya +' '+ familia, button='Пока, я буду скучать')
