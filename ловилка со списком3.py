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
            self.x = self.x+1
        else:
            pass
    def left(self):
        if self.x>0:
            self.x = self.x-1
        else:
            pass
    def touch(self, spicok):
        pass
        
pole = [['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','O','*','*','*','*']]
drops = []
for step in range(3):
    drops.append(Drop('b'))
    drops.append(Drop('$'))

kb.add_hotkey('left', left)
kb.add_hotkey('right', right)
bomba = Drop('b')
while True:
    bomba.go()
    print('y=',bomba.y)
    print('timer=',bomba.timer)
    print('visible=',bomba.visible)
    print(" ")
    time.sleep(2)