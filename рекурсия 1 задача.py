num = int(input('Введите число:'))


def print_num(num):
    if num == 1:
        print(1)
    else:
        print_num(num-1)
        print(num)
        
        
print_num(num)
        
        
