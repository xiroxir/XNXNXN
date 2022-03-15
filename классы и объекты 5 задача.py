class Class():
    def __init__(self, a=6,b=3):
        self.number = a
        self.umber = b
    def __del__(self):
        print('ААА, за что:')

cucu = Class(7,4)
del cucu