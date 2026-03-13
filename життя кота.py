import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.hunger = 0
        self.alive = True

    def to_eat(self):
        print("Час їсти")
        self.hunger -= 5
        self.gladness += 2

    def to_sleep(self):
        print("Час спати")
        self.gladness += 5
        self.hunger += 2

    def to_play(self):
        print("Час гратися")
        self.gladness += 10
        self.hunger += 5

    def is_alive(self):
        if self.hunger > 20:
            print("Тваринка дуже голодна...")
            self.alive = False
        elif self.gladness < 0:
            print("Депресія...")
            self.alive = False

    def end_of_day(self):
        print(f"Задоволення = {self.gladness}")
        print(f"Голод = {self.hunger}")

    def live(self, day):
        print(f"--- День {day} життя {self.name} ---")
        choice = random.randint(1, 3)
        if choice == 1:
            self.to_eat()
        elif choice == 2:
            self.to_sleep()
        elif choice == 3:
            self.to_play()
        self.end_of_day()
        self.is_alive()

my_pet = Pet(name="Барсик")

for day in range(1, 366):
    if my_pet.alive == False:
        print(f"{my_pet.name} більше не може продовжувати.")
        break
    my_pet.live(day)
    