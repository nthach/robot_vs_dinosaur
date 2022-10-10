
from dinosaur import Dinosaur
from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Sword", 24)
    
        


    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.active_weapon.attack_power
        print("Dinosaur's Health: " + str(dinosaur.health))