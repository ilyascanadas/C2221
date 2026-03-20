import random

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.fuel = 100
        self.condition = 100

    def drive(self):
        if self.fuel > 0 and self.condition > 0:
            print(f"Машина {self.brand} їде.")
            self.fuel -= 10
            self.condition -= 5
            return True
        else:
            print(f"Машина {self.brand} не може їхати.")
            return False

class Human:
    def __init__(self, name, car):
        self.name = name
        self.car = car
        self.money = 50

    def work(self):
        if self.car.drive():
            self.money += 20
            print(f"{self.name} поїхав на роботу і заробив грошей.")
        else:
            print(f"{self.name} не зміг поїхати на роботу.")

    def repair_car(self):
        if self.money >= 30:
            self.money -= 30
            self.car.condition = 100
            self.car.fuel = 100
            print(f"{self.name} відремонтував та заправив машину.")
        else:
            print(f"У {self.name} недостатньо грошей для ремонту.")

my_car = Car("BMW")
me = Human("Reder", my_car)

for day in range(1, 6):
    print(f"--- День {day} ---")
    action = random.randint(1, 2)
    if action == 1:
        me.work()
    else:
        me.repair_car()
    print(f"Гроші: {me.money}, Паливо: {me.car.fuel}, Стан: {me.car.condition}%")
    