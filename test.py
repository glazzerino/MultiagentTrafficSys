
from model.TrafficModel import TrafficModel
import agentpy as ap
import matplotlib.pyplot as plt
import numpy as np
import IPython
print("**Multiagent Traffic System Simulator**")
print("Team No.6")

# Parameters
parameters = {
    "size" : 40,
    "cars" : 10,
    "lights" : 2,
    "max_inertia" : 2,
    "max_humans": 12,
    "safe_distance": 4,
    "steps": 100,
}

tModel = TrafficModel(parameters)
tModel.steps = 100
tModel.setup()
tModel.run()
def my_plot(m, ax):
    ax.set_title("Traffic Model")
    ax.set_xlim([0, parameters["size"]])
    ax.set_ylim([0, parameters["size"]])
    ax.set_xticks(np.arange(0,parameters["size"], 1))
    ax.set_yticks(np.arange(0,parameters["size"], 1))
    ax.grid(True)
    pos = m.space.positions.values()
    pos = np.array(list(pos)).T
    ax.scatter(*pos, s=5, c='black')
    ax.set_aspect('equal')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

def animation():
    fig, ax = plt.subplots()
    anim = ap.animate(tModel,fig, ax, my_plot)
    return IPython.display.HTML(anim.to_jshtml(fps=60))
   