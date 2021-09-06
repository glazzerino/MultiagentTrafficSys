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
from utils.orientation import ORIENTATION

class TrafficModel(agentpy.Model):

    def setup(self):
        self.cars = agentpy.AgentList(self, self.p.cars, Car)
        self.lights = agentpy.AgentList(self, self.p.lights, TrafficLight)
        self.space = Space(self, shape=[self.p.size] * 2) # 2D space 

        human_count = random.randint(0, self.p.max_humans)
        self.humans = agentpy.AgentList(self, human_count, Human)
        self.stepcount = 0
        self.lights[0].set_orientation(ORIENTATION.H)
        self.lights[1].set_orientation(ORIENTATION.V)
        self.set_agent_coords()
        self.diagonal = MathUtils.hypoth(self.p.size)
        for car in self.cars:
            car.set_safe_dist(self.p.safe_distance)
            if car.get_orientation() == ORIENTATION.H:
                car.set_light(self.lights[0])
            else:
                car.set_light(self.lights[1])
        print("Cars set up")
        # Register traffic lights their coutnerpart
        self.lights[0].set_counterpart(self.lights[1])
        self.lights[1].set_counterpart(self.lights[0])
        print("Traffic lights set up")

    def step(self):
        self.stepcount += 1
        self.lights.step()
        for car in self.cars:
            mindistance = self.diagonal
            for n in self.cars:
                if car == n:
                    continue
                if n.get_orientation() == car.get_orientation():
                    # Check if car is atually in front of ours and keep it if its immediatly in front 
                    # sry por la mega linea
                    if (n.get_orientation == ORIENTATION.H and n.get_position()[1] > car.get_position()[1]) or n.get_orientation() == ORIENTATION.V and n.get_position()[0] < car.get_position()[0]:
                        distance = MathUtils.dist(n.get_position(), car.get_position())
                        if distance < mindistance:
                            mindistance = distance
         
            car.calc_speed(mindistance)
            car.move()
        self.lights.step()
                
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

    def reset_stepcount(self):
        self.stepcount = 0