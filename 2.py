class Road:
    _length = 0
    _width = 0
    _cm = 0
    def __init__(self, length, width, cm):
        self.length = length
        self.width = width
        self.cm = cm
    def calc(self):
        print(int(self.length) * int(self.width) * int(self.cm))

a = Road(10, 10, 5)
a.calc()