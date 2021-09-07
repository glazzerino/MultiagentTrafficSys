import random
from agents.TrafficLight import TrafficLight
import agentpy as ap
from enum import Enum
from agents.TrafficLight import Color
from utils.orientation import ORIENTATION
import numpy

class MODEL_TYPE(Enum):
    CAR = 0
    TRUCK = 1
    BUS = 2

class Car(ap.Agent):
    def setup(self):

        self.mass = random.randint(1, 2)
        self.velocity = 0
        # Set model type as a random number between 0 and 2
        self.type = MODEL_TYPE(random.randint(0, 2))

        self.direction = random.randint(0, 1)
        self.max_speed = self.p.max_inertia / self.mass
        self.light = None 
        self.orientation = random.randint(0, 1)
        if self.orientation == 1:
            self.orientation = ORIENTATION.H 
        else:
            self.orientation = ORIENTATION.V 
        # Print data of the car
        self.next_car = None
        self.print_data()

    def set_safe_dist(self, safe_dist):
        self.safe_dist = safe_dist

    def print_data(self):
        print("Car: mass:", self.mass, "type:", self.type, "direction:", self.direction) 
        print("----")
    
    def set_position(self, space: ap.Space):
        self.space = space
        self.position = space.positions[self]

    def vel_to_vec(self, velocity):
        if self.orientation == ORIENTATION.H:
            velocity = [0, velocity]
        else:
            velocity = [velocity, 0]
        return velocity

    def get_orientation(self): 
        return self.orientation
    
    def set_space(self, space: ap.Space):
        self.space = space

    def get_position(self):
        return self.space.positions[self]

    def past_light(self):
        lightpos = self.light.get_pos()
        if self.orientation == ORIENTATION.H:
            return self.get_position()[1] > lightpos[1]
        else:
            return self.get_position()[0] < lightpos[0]

    def set_next_car(self, car: ap.Agent):
        self.next_car = car

    def calc_speed(self, distance: float):
        if (self.light.get_state() != Color.RED or self.past_light()) and distance > self.p.safe_distance:
            if self.next_car is not None:
                self.velocity = self.vel_to_vec(min(self.max_speed, self.next_car.max_speed))
            else:
                self.velocity = self.vel_to_vec(self.max_speed)
        else:
            self.velocity = [0, 0]

    def move(self):
        self.space.move_by(self, self.velocity)

    def set_orientation(self, orientation: ORIENTATION):
        self.orientation = orientation
    
    def set_light(self, light: TrafficLight):
        self.light = light
