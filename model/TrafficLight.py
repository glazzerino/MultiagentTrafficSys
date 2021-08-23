import agentpy as ap
from enum import Enum
class TrafficLight(ap.Agent):
    class Color(Enum):
        RED = 0
        YELLOW = 1
        GREEN = 2
    def setup(self):
        self.state = Color.red
        