spicok = [['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*']]
yO = 0
xO = 0
comand = input('Введите команду:')
while comand != 'Выход':
    spicok[yO][xO] = '*'
    if comand == 'Вправо':
        if xO != 9:
            xO = xO + 1
            spicok[yO][xO] = 'O'
            for pipi in spicok:
                for pypy in pipi:
                    print(pypy + " ", end='')
                print()
        else:
            print('Отстань')
    elif comand == 'Влево':
        if xO != 0:
            xO = xO - 1
            spicok[yO][xO] = 'O'
            for pipi in spicok:
                for pypy in pipi:
                    print(pypy + " ", end='')
                print()
        else:
            print('Отстань')
    elif comand == 'Вверх':
        if yO != 0:
            yO = yO - 1
            spicok[yO][xO] = 'O'
            for pipi in spicok:
                for pypy in pipi:
                    print(pypy + " ", end='')
                print()
        else:
            print('Отстань')
    elif comand == 'Вниз':
        if yO != 9:
            yO = yO + 1
            spicok[yO][xO] = 'O'
            for pipi in spicok:
                for pypy in pipi:
                    print(pypy + " ", end='')
                print()
        else:
            print('Отстань')
    comand = input('Введите команду:')
print('Конец')