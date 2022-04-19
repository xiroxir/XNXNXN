import random
game = True
pole = [["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"]]

vidimost_polya=[["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"]]



def vyvodPolya(spisok):
    for stroka in spisok:
        for kletka in stroka:
            print(kletka,end='')
        print()
        
def mingenerator(pole):
    Xmina = random.randint(0,11)
    Ymina = random.randint(0,11)
    pole[Ymina][Xmina] = "O"
    Xmina = random.randint(0,11)
    Ymina = random.randint(0,11)
    pole[Ymina][Xmina] = "O"
    Xmina = random.randint(0,11)
    Ymina = random.randint(0,11)
    pole[Ymina][Xmina] = "O"
    
def proverka(pole):
    for stroka in range(12):
        for stolb in range(12):
            setchik = 0
            if stroka-1 >= 0:
                if pole[stroka-1][stolb]== "O":
                    setchik = setchik+1
                if stolb-1 >= 0:
                    if pole[stroka-1][stolb-1]=="O":
                        setchik = setchik+1
                if stolb+1 < len(pole[stroka]):
                    if pole[stroka-1][stolb+1]=="O":
                        setchik = setchik+1
                    
            if stroka+1 < len(pole):
                if pole[stroka+1][stolb] == "O":
                    setchik = setchik+1
                if stolb-1 >= 0:
                    if pole[stroka+1][stolb-1]=="O":
                        setchik = setchik+1
                if stolb+1 < len(pole[stroka]):
                    if pole[stroka+1][stolb+1]=="O":
                        setchik = setchik+1
                    
            if stolb-1 >= 0:
                    if pole[stroka][stolb-1]=="O":
                        setchik = setchik+1
            if stolb+1 < len(pole[stroka]):
                if pole[stroka][stolb+1]=="O":
                    setchik = setchik+1
            if setchik != 0:
                pole[stroka][stolb]=str(setchik)


def check(stroka,stolb):
    
    if vidimost_polya[stroka][stolb] == "•":
        vidimost_polya[stroka][stolb] = pole[stroka][stolb]
        if pole[stroka][stolb] == "*":
            if stroka-1 >= 0:
                check(stroka-1,stolb)
                if stolb-1 >= 0:
                    check(stroka-1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka-1,stolb+1)
                    
            if stroka+1 < len(pole):
                check(stroka+1,stolb)
                if stolb-1 >= 0:
                    check(stroka+1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka+1,stolb+1)
                    
            if stolb-1 >= 0:
                    check(stroka,stolb-1)
            if stolb+1 < len(pole[stroka]):
                check(stroka,stolb+1)
        elif pole[stroka][stolb] == "O":
            game = False
                
                
def isOpen():
    opened = True
    for stroka in vidimost_polya:
        if "•" in stroka:
            opened = False
    return opened



print("Всё поле открыто!")