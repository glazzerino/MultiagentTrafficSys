import math

class MathUtils:
   def dist(a: tuple, b:tuple):
      return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
   
   def hypoth(s: int):
      return math.sqrt((s**2) * 2)