import agentpy
import numpy as np
import model.TrafficLight
import agents.Car
class TrafficModel(agentpy.Model):

    def setup(self):
       self.matrix = np.zeros((self.p.size, self.p.size) )
       self.agents = agentpy.AgentList(self, self.p.number_of_agents, Car.Car)
       self.lights = agentpy.AgentList(self, self.p.number_of_lights, model.TrafficLight.TrafficLight)

       

       
            

