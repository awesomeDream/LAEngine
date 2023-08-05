import pygame

from mathlib import Vector2D

BLACK = (0, 0, 0)
INF = 10000000000

class Polygon:
  def __init__(self, pos, points):
    self.pos = pos
    
    self.__points = points
    self.__angle = 0
    
    self.__updateRotated()
  
  def rotate(self, ang):
    self.angle += ang
    self.__updateRotated()
    
  def __updateRotated(self):
    self.rotated = [v.rotate(self.__angle) for v in self.__points]
    
  def getRect(self):
    max_x, max_y, min_x, min_y = -INF, -INF, INF, INF

    for r in self.rotated:
      if max_x < r.x: max_x = r.x
      if max_y < r.y: max_y = r.y
      if min_x > r.x: min_x = r.x
      if min_y > r.y: min_y = r.y
    
    return Rect(min_x + self.pos.x, min_y + self.pos.y, max_x - min_x, max_y - min_y)

  def draw(self, screen, camera, color = BLACK):
    pygame.draw.lines(screen, color, True, [(p + self.pos - camera.padding()).toTuple() for p in self.rotated])
    

class Rect:
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
  
  def draw(self, screen, color = BLACK):
    pygame.draw.rect(screen, color, (self.x, self.y, self.w, self.h), 1)

class Circle:
  def __init__(self, pos, radius):
    self.pos = pos
    self.radius = radius
    
  def getRect(self):
    return Rect(self.pos.x - self.radius, self.pos.y - self.radius, self.radius + self.radius, self.radius + self.radius)
  
  def draw(self, screen, camera, color = BLACK):
    pygame.draw.circle(screen, color, (self.pos - camera.padding()).toTuple(), self.radius, 1)