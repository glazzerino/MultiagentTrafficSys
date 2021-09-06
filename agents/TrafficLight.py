from __future__ import annotations
import agentpy as ap
from enum import Enum
from agents.Human import Human
from utils.orientation import ORIENTATION


class Color(Enum):
    RED = 0
    GREEN = 1
    YELLOW = 2


class TrafficLight(ap.Agent):

    def setup(self):
        self.state = Color.RED
        self.vehicle_count = 0
        self.counterpart = None
        self.clock = 1
        # self.humans = ap.AgentList(self, 4, Human)

    def add_vehicle(self):
        self.vehicle_count += 1

    def remove_vehicle(self):
        self.vehicle_count -= 1

    def reset_vehicle_count(self):
        self.vehicle_count = 0

    def update(self):
        if self.state == Color.GREEN:
            self.state = Color.YELLOW
        elif self.state == Color.YELLOW:
            self.state = Color.RED
        elif self.state == Color.RED:
            self.state = Color.GREEN

    def get_state(self):
        return self.state

    def set_position(self, space: ap.Space):
        self.space = space
        self.pos = space.positions[self]

    def set_orientation(self, o: ORIENTATION):
        self.orientation = o

    def set_counterpart(self, c: TrafficLight):
        self.counterpart = c

    def step(self):
        if self.model.stepcount < 10:
            return
        else:
            self.update()

    def get_pos(self):
        return self.model.space.positions[self]
