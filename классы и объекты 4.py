class Setchik:
    def __init__ (self,a):
        self.number = a
    def ymen(self):
        self.number=int(self.number) - 1
    def bols(self):
        self.number=int(self.number) + 1
    def vivod(self):
        print(self.number)
a= input('Введите число:')
cucu = Setchik(a)
comand = input('Введите команду:')
while True:
    if comand == 'ymen':
        cucu.ymen()
    elif comand == 'bols':
        cucu.bols()
    elif comand == 'vivod':
        cucu.vivod()
    comand = input('Введите команду:')