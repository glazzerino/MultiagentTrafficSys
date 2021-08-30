import agentpy as ap
from enum import Enum
from agents.Human import Human
class Color(Enum):
    RED = 0
    GREEN = 1
    YELLOW = 2

class TrafficLight(ap.Agent):

    def setup(self):
        self.state = Color.RED
        self.vehicle_count = 0
        # self.humans = ap.AgentList(self, 4, Human)

    def add_vehicle(self):
        self.vehicle_count += 1

    def remove_vehicle(self):
        self.vehicle_count -= 1

    def reset_vehicle_count(self):
        self.vehicle_count = 0

    def update(self):
        self.state += 1 # red -> green -> yellow -> red ...
        if self.state > 2:
            self.state = 0

    def get_state(self):
        return self.state
    
    def set_position(self, space: ap.Space):
        self.space = space
        self.pos = space.positions[self]
     
