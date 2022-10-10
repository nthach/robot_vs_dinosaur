
import random
from secrets import choice
from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot("Other JJ")
        self.dinosaur = Dinosaur("JJ", 25)
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')
       
    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            choice = random.randint(1,2)
            if choice == 1:
                print("Robot's turn to attack")
                self.robot.attack(self.dinosaur)
            else:
                print("Dinosaur's turn to attack")
                self.dinosaur.attack(self.robot)

    def display_winner(self):
        if self.robot.health <= 0:
            print("The winner is: Dinosaur!")

        else:
            print("Robot wins!")    
    
