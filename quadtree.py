from shape import Rect
from collision import AABB

CAPACTIY = 5
MAX_DEPTH = 10

class QuadTree:
  def __init__(self, boundary, depth = 1):
    self.boundary = boundary
    self.shapes = []
    self.splited = False
    self.depth = depth
  
  def __split(self):
    if self.splited:
      return
    
    self.splited = True
    
    x, y, w, h, d = self.boundary.x, self.boundary.y, self.boundary.w / 2, self.boundary.h / 2, self.depth + 1

    self.childs = [
      QuadTree(Rect(x, y, w, h), d),
      QuadTree(Rect(x + w, y, w, h), d),
      QuadTree(Rect(x, y + h, w, h), d),
      QuadTree(Rect(x + w, y + h, w, h), d)
    ]
    
  def insert(self, shape):
    if not AABB(self.boundary, shape.getRect()):
      return False
    
    if len(self.shapes) < CAPACTIY:
      self.shapes.append(shape)
      return True
    
    if self.depth < MAX_DEPTH and not self.splited:
      self.__split()
    
    b = False

    for child in self.childs:
      if child.insert(shape):
        b = True
      
    return b
  
  def search(self, query_rect, out_list):
    if not AABB(self.boundary, query_rect):
      return
    
    for s in self.shapes:
      #if id(s) == id(shape):
      #  continue
      
      if AABB(query_rect, s.getRect()) and not s in out_list:
        out_list.append(s)
    
    if not self.splited:
      return
    
    for child in self.childs:
      child.search(query_rect, out_list)
      
  def draw(self, screen):
    print(self.boundary.x, self.boundary.y, self.boundary.w, self.boundary.h)
    self.boundary.draw(screen, (25, 60, 80))
    
    if not self.splited:
      return
    
    for child in self.childs:
      child.draw(screen)