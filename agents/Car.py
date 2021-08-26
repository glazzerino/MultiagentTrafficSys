import random
import agentpy
from enum import Enum

from agentpy import agent

class MODEL_TYPE(Enum):
    CAR = 0
    TRUCK = 1
    BUS = 2
class Car(agentpy.Agent):

    def setup(self):
        # Set mass as a random number between 1 and 10
        self.mass = random.randint(1, 10)
        
        # Set model type as a random number between 0 and 2
        self.type = MODEL_TYPE(random.randint(0, 2))

        self.direction = random.randint(0, 1)
        self.max_speed = self.p.max_inertia / self.mass

        # Print data of the car
        self.print_data()

    def print_data(self):
        print("Car: mass:", self.mass, "type:", self.type, "direction:", self.direction) 
        print("----")
    
