import agentpy as ap
from agents.TrafficLight import TrafficLight
from utils.orientation import ORIENTATION
import random

class Walker(ap.Agent):
   def setup(self):
      self.orientation = None
      surprise = ""
      self.destination = None
      if random.randint(0,1) == 1:
         surprise = ", it's a cow"
      print("Walker set up"+surprise)

   def set_light(self, light: TrafficLight): 
      self.light = light
   
   def set_orientaiton(self, orientation: ORIENTATION):
      self.orientation = orientation
      # Set destination depending on whether its a vertical or horizontal orientation
         
