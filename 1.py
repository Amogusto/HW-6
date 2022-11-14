import time


class Trafficlight:
    __color = "green"

    def running(self):
        Trafficlight.color = "Red"
        print(self.color)
        time.sleep(7)
        Trafficlight.color = "Yellow"
        print(self.color)
        time.sleep(3)
        Trafficlight.color = "Green"
        print(self.color)
        time.sleep(9)


a = Trafficlight()
a.running()
