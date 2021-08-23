from model.TrafficLight import TrafficLight
import model.TrafficModel as TrafficModel
import time
print("**Multiagent Traffic System Simulator**")
print("Team No.6")
# Parameters
parameters = {
    "size" : 20,
    "number_of_agents" : 10,
}
env = TrafficModel.TrafficModel(parameters)
env.setup()
# Main loop
while(True):
    # El servidor duerme por 3 segundos 
    time.sleep(3)
