import agentpy
import numpy as np
import model.TrafficLight
class Env(agentpy.Model):

    def setup(self):
       self.matrix = np.zeros((self.p.size, self.p.size) )
       self.agents = agentpy.AgentList(self, self.p.number_of_agents)

       
            

