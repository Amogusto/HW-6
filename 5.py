class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Запуск отрисовки карандашом")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Запуск отрисовки маркером")

a = Pencil("asd")
b = Pen("DSD")
c = Handle("DASD")
a.draw()
b.draw()
c.draw()