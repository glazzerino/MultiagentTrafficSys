import random
import agentpy as ap
from enum import Enum
import numpy


class MODEL_TYPE(Enum):
    CAR = 0
    TRUCK = 1
    BUS = 2
class ORIENTATION(Enum):
    H = 0
    V = 1,
class Car(ap.Agent):
    def setup(self):
        # Set mass as a random number between 1 and 10
        self.mass = random.randint(1, 10)
        self.velocity = 3
        # Set model type as a random number between 0 and 2
        self.type = MODEL_TYPE(random.randint(0, 2))

        self.direction = random.randint(0, 1)
        self.max_speed = self.p.max_inertia / self.mass

        self.orientation = random.randint(0, 1)
        if self.orientation == 1:
            self.orientation = ORIENTATION.H 
        else:
            self.orientation = ORIENTATION.V 
        
        # Print data of the car
        self.print_data()

    def print_data(self):
        print("Car: mass:", self.mass, "type:", self.type, "direction:", self.direction) 
        print("----")
    
    def set_position(self, space: ap.Space):
        self.space = space
        self.position = space.positions[self]

    def get_orientation(self): 
        return self.orientation
    
