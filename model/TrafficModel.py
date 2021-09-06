import agentpy
from agentpy.space import Space
from matplotlib import pyplot as plt
import numpy as np
from agents.Car import Car
from agents.TrafficLight import TrafficLight
from agents.Human import Human
import random
import matplotlib 
from utils.mathutils import MathUtils 
from agents.Car import ORIENTATION

class TrafficModel(agentpy.Model):

    def setup(self):
        self.cars = agentpy.AgentList(self, self.p.cars, Car)
        self.lights = agentpy.AgentList(self, self.p.lights, TrafficLight)
        self.space = Space(self, shape=[self.p.size] * 2) # 2D space 

        human_count = random.randint(0, self.p.max_humans)
        self.humans = agentpy.AgentList(self, human_count, Human)

        self.lights[0].set_orientation(ORIENTATION.H)
        self.lights[1].set_orientation(ORIENTATION.V)
        self.set_agent_coords()
        self.diagonal = MathUtils.hypoth(self.p.size)
        self.cars.set_safe_dist(self.p.safe_distance)

    def step(self):
        for car in self.cars:
            mindistance = self.diagonal
            nearest_car = None
            for n in self.cars:
                if car == n:
                    continue
                if n.get_orientation() == car.get_orientation() and (car.get_position()[1] < n.get_position()[1] or car.get_position()[0] < n.get_position()[0]):
                    distance = MathUtils.dist(n.get_position(), car.get_position())
                    if distance < mindistance:
                        mindistance = distance
                        nearest_car = n
         
            car.calc_speed(mindistance)
            car.move()
                
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
        self.cars.set_space(self.space)

        # Set lights (only two)
        lightpositions = []
        lightpositions.append([intersect_size, intersect_size])
        lightpositions.append([intersect_size, self.p.size - intersect_size])
        self.space.add_agents(self.lights, lightpositions)

