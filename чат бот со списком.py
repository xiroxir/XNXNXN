cpicok = []
comand = 0
play = 0
pmchim = 0
print("Чтобы начать общаться с чат-ботом напишите play")
play = input("Введите play:")
if play == "play":
    comand = input('Введите команду:').lower
    while comand != 'exit':
        if comand == 'добавить':
            num1 = input('Введите, что хотите добавить:')
            cpicok.append(num1)
            print('Элемент успешно добавлен')
        elif comand == 'удалить':
            num2 = input('Введите, что хотите удалить:')
            if num2 in cpicok:
                cpicok.remove(num2)
                print('Элемент успешно удалён')
            else:
                print('В вашем списке нету такого элемента')
        elif comand == 'показать весь список':
            for cpic in cpicok:
                print(cpic)
        elif comand == 'показать элемент по номеру':
            num3 = input('Введите номер, чтобы узнать, что это в списке:')
            try:
                print(cpicok[int(num3)-1])
            except:
                print('Такого элемента не обнаружено в этом списке')
        elif comand == 'редактировать список по номеру':
            num4 = input('Введите номер, который хотите редактировать:')
            redak1 = input('Введите слово, на которое вы хотите заменить:')
            try:
                cpicok[int(num4)-1] = redak1
                print('Элемент успешно отредактирован')
            except:
                print('Такого элемента не обнаружено в этом списке')
        elif comand == 'редактировать элемент списка по имени':
            num5 = input('Введите имя элемента, который хотите отредактировать:')
            redak2 = input('Введите имя элемента, на что вы хотите отредактировать:')
            if num5 in cpicok:
                for i in range (0, len(cpicok)):
                    if list[i]==num5:
                        list[i]=redak2
                        print('Элемент успешно отредактирован')
                    else:
                        print('Упс, что-то пошло не так')
        else:
            print('Данной команды не обнаружено')
        comand = input('Введите команду:')        