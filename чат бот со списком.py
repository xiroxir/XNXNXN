cpicok = []
comand = 0
play = 0
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
            num3 = input('Введите число:')
            try:
                print(cpicok[int(num3)-1])
            except:
                print('Такого элемента не обнаружено в этом списке')
        else:
            print('Данной команды не обнаружено')
        comand = input('Введите команду:')