from model.TrafficModel import TrafficModel
import agentpy as ap
import matplotlib.pyplot as plt
import numpy as np
import IPython
print("**Multiagent Traffic System Simulator**")
print("Team No.6")

# Parameters
parameters = {
    "size" : 20,
    "number_of_agents" : 10,
    "number_of_lights" : 2,
    "max_inertia" : 2,
}

model = TrafficModel(parameters)
model.setup()

def my_plot(model, ax):
    ax.set_title("Traffic Model")
    ax.set_xlim([0, 20])
    ax.set_ylim([0, 20])
    ax.set_xticks(np.arange(0,20, 1))
    ax.set_yticks(np.arange(0,20, 1))
    ax.grid(True)
    ax.set_aspect('equal')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.clear()

def animation():
    fig, ax = plt.subplots()
    anim = ap.animate(model,fig, ax, my_plot)
    return IPython.display.HTML(anim.to_jshtml(fps=20))
animation()