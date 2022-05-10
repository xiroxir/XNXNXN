import random
import time
import keyboard as kb
class Drop:
    def __init__(self, s):
        self.x = random.randint(0, 8)
        self.y = 0
        self.timer = random.randint(1, 7)
        self.visible = False
        self.snachok = s
    def fall(self):
        self.y = self.y + 1
        if self.y == 10:
            self.y = 0
            self.timer = random.randint(1, 7)
            self.visible = False
    def countdown(self):
        if self.visible == False:
            self.timer = self.timer - 1
            if self.timer == 0:
                self.visible = True
    def go(self):
        if self.visible == False:
            self.countdown()
        else:
            self.fall()
class Player:
    def __init__(self):
        self.x = 4
        self.y = 9
        self.hp = 3
        self.ochki = 0
    def right(self):
        if self.x < 8:
            self.x = 1
        else:
            pass
    def left(self):
        if self.x>0:
            self.x = -1
        else:
            pass
    def touch(self, spicok):
        pass
    
class Pole:
    def __init__(self):
        self.pole = [['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','O','*','*','*','*']]
    def otris(self, drops, player):
        self.pole=[['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*']]
        self.pole[player.y][player.x] = "O"
        for drop in drops:
            if drop.visible = True:
                self.pole[drop.y][drop.x] = drop.snachok
        for pipi in self.pole:
            for pypy in pipi:
                print(pypy + " ", end='')
            print()
        print() 

drops = []
for step in range(3):
    drops.append(Drop('b'))
    drops.append(Drop('$'))

player = Player()
pole = Pole()
kb.add_hotkey('left', player.left)
kb.add_hotkey('right', player.right)
#bomba = Drop('b')
while True:
    for drop in drops:
        drop.go()
    pole.otris(drops, player)
    time.sleep(1)