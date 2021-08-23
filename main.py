from model.TrafficLight import TrafficLight
from model.TrafficModel import TrafficModel

import time
print("**Multiagent Traffic System Simulator**")
print("Team No.6")
# Parameters
parameters = {
    "size" : 20,
    "number_of_agents" : 10,
    "number_of_lights" : 2,
}

env = TrafficModel(parameters)
env.setup()
# Main loop

while(True):
    # The server sleeps 
    time.sleep(1)
    env.step()
