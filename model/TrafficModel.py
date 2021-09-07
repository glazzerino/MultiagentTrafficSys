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
from agents.TrafficLight import Color

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
        self.lights[0].set_color(Color.RED)
        self.lights[1].set_color(Color.GREEN)
        print("Traffic lights set up")

    def step(self):
        self.stepcount += 1
        self.lights.step()
        for car in self.cars:
            mindistance = self.diagonal
            proximate_car = None
            for n in self.cars:
                if car == n:
                    continue
                npos = n.get_position()
                carpos = car.get_position()
                # Refactor later
                if n.get_orientation() == car.get_orientation() == ORIENTATION.H:
                    if carpos[1] == npos[1] and carpos[0] < npos[0]:
                        distance = npos[0] - carpos[0] 
                        if distance < mindistance:
                            mindistance = distance
                            car.set_next_car(n)
                if n.get_orientation() == car.get_orientation() == ORIENTATION.V:
                    if carpos[0] == npos[0] and carpos[1] < npos[1]:
                        distance = npos[1] - carpos[1] 
                        if distance < mindistance:
                            mindistance = distance
                            car.set_next_car(n)
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