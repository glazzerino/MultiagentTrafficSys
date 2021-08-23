import agentpy
from agentpy.space import Space
import numpy as np
from model.Car import Car
from model.TrafficLight import TrafficLight
import matplotlib.pyplot as plt

class TrafficModel(agentpy.Model):

    def setup(self):
        self.matrix = np.zeros((self.p.size, self.p.size) )
        self.cars = agentpy.AgentList(self, self.p.number_of_agents, Car)
        self.lights = agentpy.AgentList(self, self.p.number_of_lights, TrafficLight)
        
        # Instantiate continous space
        self.space = Space(self, shape=[self.p.size] * 2) # 2D space 
        self.position_agents()

    def step(self):
        for car in self.cars:
            car.print_data()

    def position_agents(self):
        self.space.add_agents(self.cars)
        # Define starting position for each car
        positions_car = []
        for i in range(self.p.number_of_agents):
            # Variable used to decide staring street of each car
            random_decision = np.random.randint(0, 3)
            # Define starting position for each car
            if random_decision == 0:
                positions_car.append([0, i])
            if random_decision == 1:
                positions_car.append([self.p.size - 1, i])
            if random_decision == 2:
                positions_car.append([i, 0])
            if random_decision == 3:
                positions_car.append([i, self.p.size - 1])
        
        positions_lights = [[1, 1], [0, 0]]
        self.space.add_agents(self.lights, positions_lights)
        self.space.add_agents(self.cars, positions_car)

    def draw(self, ax):
        ax.clear()
        ax.set_title("Traffic System Simulator")
        pos = self.space.position.values()
        pos = np.array(list(pos)).T 
        ax.scattter(*pos, s=1, c="b")
        ax.set_xlim(0, self.p.size)
        ax.set_ylim(0, self.p.size)
        ax.set_axis_off()
