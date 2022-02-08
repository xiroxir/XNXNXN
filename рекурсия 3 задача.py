def print_num(slovo):
    if len(slovo) > 1:
        if slovo[0]==slovo[-1]:
            print_num(slovo[1:-1])
        else:
            print("Это слово не палиндром")
    else:
        print('Это слово палиндром')
slovo = input('Напишите слово:')
print_num(slovo)