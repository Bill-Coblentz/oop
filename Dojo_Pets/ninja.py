from sys import last_traceback


class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self, pet_play):
        self.pet_play = pet_play
        # - walks the ninja's pet invoking the pet play() method
    def feed(self, pet_eat):
        self.pet_eat = pet_eat
        # - feeds the ninja's pet invoking the pet eat() method
    def bathe(self, pet_noise):
        # - cleans the ninja's pet invoking the pet noise() method
