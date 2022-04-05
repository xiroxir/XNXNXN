import mylib
mylib.mingenerator(mylib.pole)       
mylib.vyvodPolya(mylib.vidimost_polya)
mylib.game = True
while mylib.game:
    try:
        stroka = int(input("Введите номер строки"))
        stolb = int(input("Введите номер столбца"))
        mylib.check(stroka-1,stolb-1)
        mylib.vyvodPolya(mylib.vidimost_polya)
        if mylib.isOpen():
            mylib.game = False
    except:
        print("Упс, что-то пошло не так...")
    
print("Всё поле открыто!")