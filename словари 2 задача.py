pers = {"имя": "Пипя", "фамилия": "Пипяслав", "отчество": "Пипяславович", "Математика": "3", "Английский": "4", "Русский": "3"}
comand = input("Введите команду:")
while True:
    if comand == "добавить":
        new = input("Введите предмет:")
        new2 = input("Введите оценку за этот предмет:")
        pers[new] = new2
    elif comand == "изменить":
        har = input("Введите предмет:")
        har2 = input("Введите оценку, на которую хотите изменить:")
        pers[har] = har2
    elif comand == "удалить":
        delete = input("Введите предмет, который хотите удалить:")
        del pers[delete]
    elif comand == "вывести":
        for key in pers:
            print(key,": ", pers[key])
    else:
        print("Такой команды не обнаружено")
    comand = input("Введите команду:")