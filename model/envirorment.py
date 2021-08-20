import agentpy
import numpy as np

class Env(agentpy.Model):

    def setup(self):
       self.matrix = np.zeros((self.p.size, self.p.size) )
       print(self.matrix)
       self.agents = agentpy.AgentList(self, self.p.number_of_agents)
       
            


# Parameters
parameters = {
    "size" : 20,
    "number_of_agents" : 10,
}
env = Env(parameters)
env.setup()