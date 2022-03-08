class Clasno:
    def __init__(self, n, u):
        self.number = n
        self.umber = u
    def vivod(self):
        print(self.number, self.umber)
    def ismenen(self):
        self.number = input('Введите число:')
        self.umber = input('Введите число:')
    def summa(self):
        return int(self.number) + int(self.umber)
    def bolsh(self):
        if int(self.number) < int(self.umber):
            print(self.umber)
        else:
            print(self.number)

cucu = Clasno(4, 7)
cucu.vivod()
cucu.ismenen()
cucu.vivod()
print(cucu.summa())
cucu.bolsh()