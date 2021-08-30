import agentpy as ap
from enum import Enum
import random

class Direction(Enum):
   UP = 0
   DOWN = 1
   LEFT = 2
   RIGHT = 3

class Human(ap.Agent):
   def setup(self):
      print("Human is setup")
      self.type = "Human"
      self.direction = random.randint(0, 3)

   def step(self):
      dirstring = ""
      if self.direction == Direction.UP:
         self.space.moveUp(self)
         dirstring = "up"
      elif self.direction == Direction.DOWN:
         self.space.moveDown(self)
         dirstring = "down"
      elif self.direction == Direction.LEFT:
         self.space.moveLeft(self)
         dirstring = "left"
      elif self.direction == Direction.RIGHT:
         self.space.moveRight(self)
         dirstring = "right"
      else:
         print("Error: Human.step()")
      print("Human moved to " + dirstring) 