from shape import Rect
from mathlib import Vector2D

class Camera:
  def __init__(self, width, height):
    self.target = None
    self.width = width
    self.height = height
    
  def setTarget(self, target):
    self.target = target
    
  def getRect(self):
    return Rect(self.target.pos.x - self.width / 2, self.target.pos.y - self.height / 2, self.width, self.height)
  
  def padding(self):
    return self.target.pos - Vector2D(self.width / 2, self.height / 2)