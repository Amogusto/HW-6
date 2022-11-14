class Worker:
    income = {"wage": 200, "bonus": 500}
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonmus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_full_profit(self):
        return f'{sum(self._income.values())}'

John = Position('John', 'Mcclein', 'officer', 12, 78)
print(John.get_full_name())
print(John.get_full_profit())