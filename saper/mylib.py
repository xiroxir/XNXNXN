import random
game = True
pole = [["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","#","#","#","#","#"],
        ["*","*","*","#","#","#","#","#","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["#","#","#","#","*","*","*","*","*","#","#","#"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"]]

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
        
def mingenerator(spicok):
    Xmina = random.randint(0,11)
    Ymina = random.randint(0,11)
    spicok[Ymina][Xmina] = "O"
    Xmina = random.randint(0,11)
    Ymina = random.randint(0,11)
    spicok[Ymina][Xmina] = "O"
    Xmina = random.randint(0,11)
    Ymina = random.randint(0,11)
    spicok[Ymina][Xmina] = "O"

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