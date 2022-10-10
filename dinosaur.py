

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot): #passing a robot object
        ## figure out how to remove health from the 
        # robot object being printed
        robot.health = robot.health - self.attack_power
        
        #HINT: you need to use dot notation
        # to access the "health" attribute
        # Robot health is equal to
        #    robot health minus the dino's attack power
        print("Robot's Health: " + str(robot.health))
