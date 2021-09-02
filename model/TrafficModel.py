import agentpy
from agentpy.space import Space
from matplotlib import pyplot as plt
import numpy as np
from agents.Car import Car
from agents.TrafficLight import TrafficLight
from agents.Human import Human
import random
import matplotlib 

class TrafficModel(agentpy.Model):

    def setup(self):
        self.matrix = np.zeros((self.p.size, self.p.size) )
        self.cars = agentpy.AgentList(self, self.p.number_of_agents, Car)
        self.lights = agentpy.AgentList(self, self.p.number_of_lights, TrafficLight)
        self.space = Space(self, shape=[self.p.size] * 2) # 2D space 
        # Random as of now for testing purposes
        self.space.add_agents(self.lights, random=True)
        self.space.add_agents(self.cars, random=True) 

        human_count = random.randint(0, self.p.max_humans)
        self.humans = agentpy.AgentList(self, human_count, Human)

        for human in self.humans:
           which_traffic_light = random.randint(0, self.p.number_of_lights - 1)
           light = self.lights[which_traffic_light]
           pos = self.space.positions[light]
           human.set_destination(pos) 

        # Instantiate continous space
        self.cars.set_position(self.space)
        self.lights.set_position(self.space)

    def size(self):
       return self.size 

    def step(self):
        for car in self.cars:
            car.print_data()

    def set_agents(self):
        self.space.add_agents(self.cars)
        self.cars.set_position(self.space)
        # Define starting position for each car
        # positions_car = []
        # for i in range(self.p.number_of_agents):
        #     # Variable used to decide starting street of each car
        #     random_decision = np.random.randint(0, 3)
        #     # Define starting position for each car
        #     if random_decision == 0:
        #         positions_car.append([0, i])
        #     if random_decision == 1:
        #         positions_car.append([self.p.size - 1, i])
        #     if random_decision == 2:
        #         positions_car.append([i, 0])
        #     if random_decision == 3:
        #         positions_car.append([i, self.p.size - 1])
        # positions_lights = [[1, 1], [0, 0]]
        # # self.space.add_agents(self.lights, positions_lights)
        # # self.space.add_agents(self.cars, positions_car)
        # self.space.add_agents(self.lights, random=True)
        # for car in self.cars:
        #     car.set_position(self.space)
        # for traffic_light in self.lights:
        #     traffic_light.set_position(self.space)


