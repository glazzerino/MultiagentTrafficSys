import agentpy
from agentpy.space import Space
from matplotlib import pyplot as plt
import numpy as np
from agents.Car import Car
from agents.TrafficLight import TrafficLight
from agents.Human import Human
import random
import matplotlib 
from agents.Car import ORIENTATION

class TrafficModel(agentpy.Model):

    def setup(self):
        self.matrix = np.zeros((self.p.size, self.p.size))
        self.cars = agentpy.AgentList(self, self.p.cars, Car)
        self.lights = agentpy.AgentList(self, self.p.lights, TrafficLight)
        self.space = Space(self, shape=[self.p.size] * 2) # 2D space 


        human_count = random.randint(0, self.p.max_humans)
        self.humans = agentpy.AgentList(self, human_count, Human)
 
        self.set_agent_coords()
    
    def size(self):
       return self.size 

    def step(self):
        for car in self.cars:
            self.space.move_by(car, [0.3, 0.5])

    def set_agent_coords(self):
        positions = []
        intersect_size =round( self.p.size / 3)
        for car in self.cars:
            # Position is at half of space minus a random offset
            start = (self.p.size / 2) - random.randint(0, 1)
            if car.orientation == ORIENTATION.H:
                positions.append([start, random.randint(0, intersect_size)])
            else:
                positions.append([random.randint(0, intersect_size), start])
        self.space.add_agents(self.cars, positions)

        # Set lights (only two)
        lightpositions = []
        lightpositions.append([intersect_size, intersect_size])
        lightpositions.append([intersect_size, self.p.size - intersect_size])
        self.space.add_agents(self.lights, lightpositions)
