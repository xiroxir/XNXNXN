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
        try:
            xO = xO + 1
            spicok[yO][xO] = 'O'
            for pipi in spicok:
                for pypy in pipi:
                    print(pypy + " ", end='')
                print()
        except:
            print('Отстань')
        comand = input('Введите команду:')
    elif comand == 'Влево':
        try:
            xO = xO - 1
            spicok[yO][xO] = 'O'
            for pipi in spicok:
                for pypy in pipi:
                    print(pypy + " ", end='')
                print()
        except:
            print('Отстань')
        comand = input('Введите команду:')
    elif comand == 'Вверх':
        try:
            yO = yO - 1
            spicok[yO][xO] = 'O'
            for pipi in spicok:
                for pypy in pipi:
                    print(pypy + " ", end='')
                print()
        except:
            print('Отстань')
        comand = input('Введите команду:')
    elif comand == 'Вниз':
        try:
            yO = yO + 1
            spicok[yO][xO] = 'O'
            for pipi in spicok:
                for pypy in pipi:
                    print(pypy + " ", end='')
                print()
        except:
            print('Отстань')
        comand = input('Введите команду:')
print('Конец')