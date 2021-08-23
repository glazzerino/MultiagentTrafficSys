import agentpy
import numpy as np
from model.Car import Car
from model.TrafficLight import TrafficLight

class TrafficModel(agentpy.Model):

    def setup(self):
       self.matrix = np.zeros((self.p.size, self.p.size) )
       self.cars = agentpy.AgentList(self, self.p.number_of_agents, Car)
    #    self.lights = agentpy.AgentList(self, self.p.number_of_lights, TrafficLight)
    def step(self):
        for car in self.cars:
            car.print_data()
