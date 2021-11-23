import random
import keyboard as kb
import pyautogui as py
import time
cpicok = []
comand = 0
play = 0
pmchim = 0
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
    global ochki, comand
    comand = 0
    time.sleep(1)
    print(ochki)
    ochki = 0
    
kb.add_hotkey('space',proverka)
kb.add_hotkey('z', podchet)
print("Чтобы начать общаться с чат-ботом напишите play")
play = input("Введите play:")
if play == "play":
    comand = input('Введите команду:').lower()
    while comand != 'exit':
        if comand == 'список':
            comand = input('Введите команду:')
            if comand == 'добавить':
                mina1 = input('Введите, что хотите добавить:')
                cpicok.append(mina1)
                print('Элемент успешно добавлен')
            elif comand == 'удалить':
                mina2 = input('Введите, что хотите удалить:')
                if mina2 in cpicok:
                    cpicok.remove(mina2)
                    print('Элемент успешно удалён')
                else:
                    print('В вашем списке нету такого элемента')
            elif comand == 'показать весь список':
                for cpic in cpicok:
                    print(cpic)
            elif comand == 'показать элемент по номеру':
                mina3 = input('Введите номер, чтобы узнать, что это в списке:')
                try:
                    print(cpicok[int(mina3)-1])
                except:
                    print('Такого элемента не обнаружено в этом списке')
            elif comand == 'редактировать список по номеру':
                mina4 = input('Введите номер, который хотите редактировать:')
                redak1 = input('Введите слово, на которое вы хотите заменить:')
                try:
                    cpicok[int(mina4)-1] = redak1
                    print('Элемент успешно отредактирован')
                except:
                    print('Такого элемента не обнаружено в этом списке')
            elif comand == 'редактировать элемент списка по имени':
                mina5 = input('Введите имя элемента, который хотите отредактировать:')
                redak2 = input('Введите имя элемента, на что вы хотите отредактировать:')
                if mina5 in cpicok:
                    for i in range (0, len(cpicok)):
                        if cpicok[i]==mina5:
                            cpicok[i]=redak2
                            print('Элемент успешно отредактирован')
                        else:
                            print('Упс, что-то пошло не так')
            else:
                print('Данной команды не обнаружено')
            comand = input('Введите команду:')
        elif comand == 'команды':
            print('добавить', 'удалить', 'показать весь список',
                  'показать элемент по номеру', 'редактировать список по номеру',
                  'редактировать элемент списка по имени', 'однорукий бандит')
        elif comand == 'однорукий бандит':
                while comand == 'Однорукий бандит':
                    num1 = random.randint(1, 3)
                    num2 = random.randint(1, 3)
                    num3 = random.randint(1, 3)
                    print(num1, num2, num3)
                time.sleep(2)
        comand = input("Введите команду:")