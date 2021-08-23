import agentpy as ap
from enum import Enum

class TrafficLight(ap.Agent):

    class Color(Enum):
        RED = 0
        YELLOW = 1
        GREEN = 2
        
    def setup(self):
        self.state = self.Color.red
        self.vehicle_count = 0

    def add_vehicle(self):
        self.vehicle_count += 1

    def remove_vehicle(self):
        self.vehicle_count -= 1

    def reset_vehicle_count(self):
        self.vehicle_count = 0

    def update(self):
        self.Color += 1
        if self.Color > 2:
            self.Color = 0

    def get_state(self):
        return self.state
     
