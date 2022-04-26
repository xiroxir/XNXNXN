import mylib
mylib.mingenerator(mylib.pole)

mylib.vyvodPolya(mylib.vidimost_polya)

mylib.proverka(mylib.pole)
print()
while mylib.game:
    try:
        stroka = int(input("Введите номер строки"))
        stolb = int(input("Введите номер столбца"))
        mylib.check(stroka-1,stolb-1)
        print('mylib.game ',mylib.game)
        mylib.vyvodPolya(mylib.vidimost_polya)
        if mylib.isOpen():
            mylib.game = False
    except:
        print("Упс, что-то пошло не так...")
    
print("Всё поле открыто!")