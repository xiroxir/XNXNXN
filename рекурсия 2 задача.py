def print_num(A, B):
    print(A)
    if A<B:
        print_num(A+1, B)
    elif A>B:
        print_num(A-1, B)
              

C = int(input("Введите первое число:"))
D = int(input("Введите второе число:"))
 
print_num(C, D)
        