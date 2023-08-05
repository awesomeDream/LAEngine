from collision import SAT, AABB
from mathlib import Vector2D
from shape import Polygon, Circle, Rect
from quadtree import QuadTree
from camera import Camera







import pygame
import sys
import random

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Polygon with Line Method")









walls = [
  Polygon(Vector2D(200, 200), [Vector2D(50, 0), Vector2D(60, 60), Vector2D(-30, 50), Vector2D(-40, -60), Vector2D(10, -70)]),
  Polygon(Vector2D(320, 310), [Vector2D(5, -10), Vector2D(-10, 20), Vector2D(10, 5)])
]

def r(a):
  return Vector2D(random.randint(-a, a), random.randint(-a, a))

for i in range(30):
  walls.append(Polygon(r(300) + Vector2D(400, 300), [r(20), r(22), r(21)]))

for i in range(30):
  walls.append(Polygon(r(40) + Vector2D(450, 450), [r(20), r(22), r(21)]))

#for i in range(10):
#  walls.append(Circle(r(300) + Vector2D(400, 300), random.randint(3, 11)))
















poly = Circle(Vector2D(300, 300), 10)
camera = Camera(800, 600)
camera.setTarget(poly)

circles = []


import math

def drawLine(color, s, e):
  pygame.draw.line(screen, color, (s - camera.padding()).toTuple(), (e - camera.padding()).toTuple())

def algo(polygon, circle, color):
  points = [v + polygon.pos for v in polygon.rotated]
  
  ret_points = []
  inside = [False] * len(points)
  
  for i in range(len(inside)):
    diff = points[i] - circle.pos
    if diff.x * diff.x + diff.y * diff.y < circle.radius * circle.radius:
      inside[i] = True
  
  for i in range(len(points)):
    if inside[i]:
      for l in [-1, 1]:
        j = i + l 
        if j >= len(points): j = 0
        if j < 0: j = len(points) - 1
        
        diff = points[i] - circle.pos
        
        if not inside[j]:
        
          vec = (points[j] - points[i]).normalize()
          
          a = vec.x * vec.x + vec.y * vec.y
          b = vec.x * diff.x + vec.y * diff.y
          c = vec.x * diff.y - vec.y * diff.x
          
          t = (math.sqrt(circle.radius * circle.radius * a - c * c) - b) / a
          
          s = points[i]
          e = points[i] + vec * t
          
          drawLine(color, s, e)
          #pygame.draw.line(screen, color, s, e)
          ret_points.append(points[i] + vec * t)
          
        else:
          s = points[i]
          e = points[j]
          
          drawLine(color, s, e)
          #pygame.draw.line(screen, color, s, e)
  
  return ret_points

  # 선과 원이 만나는 경우를 생각 안함.
  # 원과 원의 탐색


velocity = Vector2D(0, 0)



while True:
  #t += 1
  #if t > 40:
  #  t = 0
    
  #  circles.append(Circle(poly.pos.copy(), 1))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    
    if event.type == pygame.KEYDOWN:
      
      keys = pygame.key.get_pressed()
      if keys[pygame.K_SPACE]:
        circles.append(Circle(poly.pos.copy(), 1))
      if keys[pygame.K_a]:
        velocity = Vector2D(-1, -4)
        circles.append(Circle(poly.pos.copy(), 1))
      if keys[pygame.K_d]:
        velocity = Vector2D(1, -4)
        circles.append(Circle(poly.pos.copy(), 1))
  
  speed = 1
  keys = pygame.key.get_pressed()    

  if keys[pygame.K_w]: poly.pos.y -= speed
  if keys[pygame.K_s]: poly.pos.y += speed
  if keys[pygame.K_a]: poly.pos.x -= speed
  if keys[pygame.K_d]: poly.pos.x += speed
  
  screen.fill((0, 0, 0))
   
  qt = QuadTree(Rect(0, 0, 800, 600))
  
  for wall in walls:
    qt.insert(wall)
    
  check_list = []
  qt.search(poly.getRect(), check_list)
  
  
  velocity = velocity + Vector2D(0, 0.1)
  
  poly.pos = poly.pos + velocity
  
  for check in check_list:
    collid, mtv = SAT(poly, check)
    
    if collid:
      poly.pos = poly.pos + mtv
      velocity = Vector2D(0, 0)
  
  for circle in circles:
    circle.radius += 3
    
  def chk(c):
    return c.radius < 255
  
  circles = list(filter(chk, circles))
  
    
#  for wall in walls:
#    color = (0, 255, 0) if wall in check_list else (0, 0, 0)
    
#    wall.draw(screen, color)
#    wall.getRect().draw(screen, (0, 0, 255))
  
  
  circles.sort(key = lambda c: c.radius, reverse = True)
  
  for circle in circles:
    color = (255 - circle.radius, 255 - circle.radius, 255 - circle.radius)
    
    circle_list = []
    qt.search(circle.getRect(), circle_list)
  
  
    for c in circle_list:
      color = (255 - circle.radius, 255 - circle.radius, 255 - circle.radius)
      for p in algo(c, circle, color):
        pygame.draw.circle(screen, color, (p - camera.padding()).toTuple(), 3)


    circle.draw(screen, camera, color)

  #poly.getRect().draw(screen, (0, 0, 255))
  #circle.getRect().draw(screen, (0, 0, 255))
  
  poly.draw(screen, camera, (0, 255, 0))
    
  pygame.display.flip()
  pygame.time.Clock().tick(60)