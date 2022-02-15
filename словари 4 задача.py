from operator import itemgetter
pers = [{"name": "Пипя", "rec": "17"},{"name": "Уэйн", "rec": "97"},{"name": "Дел", "rec": "57"}]
comand = input("Введите команду:")
while True:
    if comand == "добавить":
        new = input("Введите имя:")
        new2 = input("Введите рекорд:")
        pers[name] = new
        pers[rec] = new2
    elif comand == "вывести":
        pers = sorted(pers,key=itemgetter('rec'))
        for key in pers:
            print(key,": ")
    else:
        print("Я не знаю такой команды")
    comand = input("Введите команду:")


