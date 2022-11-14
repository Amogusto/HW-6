class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def showspeed(self):
        print(self.speed)


class Towncar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def showspeed(self):
        if int(self.speed) > 60:
            print("Превышение скорости")


class Sportcar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class Workcar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def showspeed(self):
        if int(self.speed) > 40:
            print("Превышение скорости")


class Policecar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


a = Car(120, "green", "niva", False)
a.go()
a.stop()
a.turn("Направо")

b = Workcar(20, "red", "Amogus", False)
b.showspeed()

c = Policecar(20, "red", "Amogus", True)
c.showspeed()
