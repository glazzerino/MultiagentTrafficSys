import agentpy as ap
from enum import Enum

class Color(Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2

class TrafficLight(ap.Agent):

    def setup(self):
        self.state = Color.RED
        self.vehicle_count = 0

    def add_vehicle(self):
        self.vehicle_count += 1

    def remove_vehicle(self):
        self.vehicle_count -= 1

    def reset_vehicle_count(self):
        self.vehicle_count = 0

    def update(self):
        self.state += 1
        if self.state > 2:
            self.state = 0

    def get_state(self):
        return self.state
     
