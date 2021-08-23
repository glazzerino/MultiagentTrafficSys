import random
import agentpy

class Car(agentpy.Agent):

    def setup(self):
        # Set mass as a random number between 1 and 10
        self.mass = random.randint(1, 10)
        # Set model type; 0 = car, 1 = truck, 2 = bus
        self.type = random.randint(0, 2)
        # 
        self.direction = random.randint(0, 1)
        # Print data of the car
        self.print_data()
    def print_data(self):
        print("Car: mass:", self.mass, "type:", self.type, "direction:", self.direction) 
    
