#from sys import last_traceback
from unicodedata import name

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self, pet_play):
        self.pet_play = pet_play
        print(pet_play + " the creature named")
        return self
    def feed(self, pet_eat):
        self.pet_eat = pet_eat
        print("Feeding " + pet_eat +"!")
        return self
    def bathe(self, pet_noise):
        self.pet_noise = pet_noise
        print(pet_noise + " cleans the ninja's pet ")
        return self

class Pet:
    def __init__(self, name, tricks):
        self.name = name
        self.tricks = tricks

    def sleep(self, sleep_bonus):
        print("increases the pets energy by " + sleep_bonus)
        return self
    def eat(self, energy_bonus):
        print("increases the pet's energy by " + energy_bonus)
        return self
    def play(self, health_bonus):
        print("increases the pet's health by " + health_bonus)
        return self
    def noise(self, sound):
        print("the pet's " + sound)
        return self

Brandon = Ninja("Brandon", "Carter", "jerky", "pork", "Rocky")
Brandon.feed("cat").walk("drag").bathe("screech")

Rocky = Pet("Rocky", "Sits")
Rocky.sleep("a little")

Brandon = Ninja("Brandon", "Carter", "jerky", "pork", Pet('Brutus', 'St. Bernard'))
print(Brandon.pet.name)