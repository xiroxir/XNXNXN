pers = {"имя": "Пипя", "возраст": "21", "рост": "183"}
comand = input("Введите команду:")
while True:
    if comand == "добавить":
        new = input("Введите какое будет свойство:")
        new2 = input("Введите значение свойства:")
        pers[new] = new2
    elif comand == "изменить":
        har = input("Введите название свойства, которое хотите изменить:")
        har2 = input("Введите то, на что вы хотите изменить:")
        pers[har] = har2
    elif comand == "вывести":
        for key in pers:
            print(key,": ", pers[key])
    else:
        print("Такой команды не обнаружено")
    comand = input("Введите команду:")