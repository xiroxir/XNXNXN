from operator import itemgetter
class Train:
    def __init__(self, n, u, t):
        self.name = n
        self.number = u
        self.time = t
spicok = []
spicok.append(Train('Unka', 7, 12))
spicok.append(Train('Kinoka', 3, 19))
spicok.append(Train('Antr', 6, 15))
spicok.append(Train('Bentra', 11, 11))
spicok.append(Train('Senyakov', 8, 10))
spicok = sorted(spicok,key=lambda object1: object1.number)
for obj in spicok:
    print(obj.name, obj.number, obj.time)