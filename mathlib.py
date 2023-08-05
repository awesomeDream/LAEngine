import math

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"Vector2D({self.x}, {self.y})"

  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    return Vector2D(self.x - other.x, self.y - other.y)

  def __mul__(self, scalar):
    return Vector2D(self.x * scalar, self.y * scalar)

  def __truediv__(self, scalar):
    return Vector2D(self.x / scalar, self.y / scalar)

  def dot(self, other):
    return self.x * other.x + self.y * other.y

  def magnitude(self):
    return math.sqrt(self.x * self.x + self.y * self.y)

  def perpendicular(self):
    return Vector2D(-self.y, self.x)
  
  def normalize(self):
    mag = self.magnitude()
    if mag != 0:
      return self / mag
    return Vector2D(0, 0)
  
  def distance_to(self, other):
    return (self - other).magnitude()

  def copy(self):
    return Vector2D(self.x, self.y)

  def rotate(self, theta):
    c = math.cos(theta * math.pi / 180)
    s = math.sin(theta * math.pi / 180)
    
    return Vector2D(c * self.x - s * self.y, s * self.x + c * self.y)

  def toTuple(self):
    return (self.x, self.y)