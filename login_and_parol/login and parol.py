print("Введите Логин и Пароль")
login = input("Введите Логин:")
parol = input("Введите Пароль:")
while login != "Suzy" or parol != "Peter":
    print("Неправильный Логин или Пароль")
    print("Введите Логин и Пароль")
    login = input("Введите Логин:")
    parol = input("Введите Пароль:")
print("Вы успешно вошли в аккаунт")
