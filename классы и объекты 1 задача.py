from operator import itemgetter
class Student:
    def __init__(self, f, i, n, b):
        self.fam = f
        self.inic = i
        self.number = n
        self.ball = b
spicok = []
spicok.append(Student('Senyakov', 'G. F.', 8, 4))
spicok.append(Student('Unka', 'A. T.', 13, 3))
spicok.append(Student('Kinoka', 'U. P.', 1, 2))
spicok.append(Student('Antr', 'L. K.', 4, 1))
spicok.append(Student('Bentra', 'S. V.', 11, 5))
spicok = sorted(spicok,key=lambda object1: object1.ball)
for obj in spicok:
    if obj.ball == 4 or obj.ball==5:
        print(obj.fam, obj.inic)