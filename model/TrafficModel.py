import agentpy
from agentpy.space import Space
from matplotlib import pyplot as plt
import json
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
        self.lights = agentpy.AgentList(self, 2, TrafficLight)
        self.space = Space(self, shape=[self.p.size] * 2)  # 2D space
        self.records = []
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
        step_snapshot = []
        print(self.log)
        self.stepcount += 1
        self.lights.step()
        for car in self.cars:
            car_snapshot = {}
            mindistance = self.diagonal
            proximate_car = None
            for n in self.cars:
                if car == n:
                    continue
                npos = n.get_position()
                carpos = car.get_position()
                # Refactor later
                # We need to compare the relevant coordinate to tell if car is on same lane
                # Default is Horizontal orientation
                caxis = 0
                naxis = 1
                if car.orientation == ORIENTATION.V:
                    caxis = 1
                    naxis = 0
                if carpos[caxis] == npos[caxis] and carpos[naxis] < npos[naxis]:
                    distance = npos[naxis] - carpos[naxis]
                    if distance < mindistance:
                        mindistance = distance
                        car.set_next_car(n)
            car.calc_speed(mindistance)
            car.move()
            car_snapshot[car.id] = [car.get_position()[0], car.get_position()[1]] 
            step_snapshot.append(car_snapshot)
        self.records.append(step_snapshot)

    def set_agent_coords(self):
        positions = []
        intersect_size = round(self.p.size / self.p.inter_size_proportion)
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

    def update(self):
        self.cars.record("position")

    def end(self):
        recordjson = json.dumps(self.records)
        # Add filesave logic here
        print(recordjson)

        with open('data.json', 'w') as json_file:
            json.dump(recordjson, json_file)
