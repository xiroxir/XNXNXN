print("Отгадай число от 1 до 10")
chislo=input("Вводи число: ")
while chislo !="7":
    print("Неправильно блин, пиши заново дурачок")
    if int(chislo)>7:
        print("ЧИСЛО МЕНЬШЕ, ЧО ТЫ ТАКИЕ БОЛЬШИЕ ЦИФРЫ ПИШЕШЬ?")
    else:
        print("НУ БОЛЬШЕ, БОЛЬШЕ, ЧО ТЫ МЕЛЬЧИШЬ?")
    chislo=input()
        
print("Да блин, как ты отгадал")
