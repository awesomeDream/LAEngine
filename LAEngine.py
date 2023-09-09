from game import Game
from shape import Rect


import pygame
import sys
import random

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Polygon with Line Method")

class Button:
  def __init__(self, s, fs, x, y, w, h):
    self.button_font = pygame.font.Font(None, fs)
    self.button_text = self.button_font.render(s, True, (0, 0, 0))
    self.button_rect = self.button_text.get_rect(center=(x, y))
    self.rect = Rect(x - w / 2, y - h / 2, w, h)
  
  def draw(self, screen):
    self.rect.draw(screen)
    screen.blit(self.button_text, self.button_rect)

  def click(self, p):
    return self.rect.point(p[0], p[1])

buttons = [
  Button("1", 30, 100, 100, 60, 60),
  Button("2", 30, 200, 100, 60, 60),
  Button("3", 30, 300, 100, 60, 60),
  Button("4", 30, 400, 100, 60, 60),
  Button("5", 30, 500, 100, 60, 60)
]

word = Button("Select any stage", 30, 400, 400, 400, 60)

game = None


while True:
  
  keys = False 
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    
    elif event.type == pygame.KEYDOWN:
      keys = pygame.key.get_pressed()
      
    elif event.type == pygame.MOUSEBUTTONDOWN:
      for i in range(len(buttons)):
        if buttons[i].click(event.pos):
          game = Game(pygame, screen, width, height, i)
          
  if game == None:
    # render stage selector
    screen.fill((30, 30, 30))
    
    for b in buttons:
      b.draw(screen)
    
    word.draw(screen)
    
  else:
    # render and update game
  
    msg = game.update(keys)
    
    if not msg == "":
      word = Button(msg, 30, 400, 400, 400, 60)
      game = None
      continue
        
    game.draw()
  
  pygame.display.flip()
  pygame.time.Clock().tick(60)
  
#   t += 0.2
  
#   v = math.sin(t)
  
#   pygame.display.flip()
#   pygame.time.Clock().tick(60)





# walls = []
# for i in a:
#   # center
#   v = Vector2D(i[0][0], i[0][1]) * 4
#   w = Vector2D(i[1][0], i[1][1]) * 4
#   u = Vector2D(i[2][0], i[2][1]) * 4
  
#   center = (v + w + u) / 3
  
#   walls.append(Polygon(center, [v - center, w - center, u - center]))

# red = []
# for i in b:
#   # center
#   v = Vector2D(i[0][0], i[0][1]) * 4
#   w = Vector2D(i[1][0], i[1][1]) * 4
#   u = Vector2D(i[2][0], i[2][1]) * 4
  
#   center = (v + w + u) / 3
  
#   red.append(Polygon(center, [v - center, w - center, u - center]))


# poly = Circle(Vector2D(370, 2060 + 50), 10)
# camera = Camera(800, 600)
# camera.setTarget(poly)

# circles = []


# import math

# def drawLine(color, s, e):
#   pygame.draw.line(screen, color, (s - camera.padding()).toTuple(), (e - camera.padding()).toTuple())

# def dist(p1, p2, center):
#   q = p2 - p1
  
#   a = q.y
#   b = -q.x
#   c = -p1.x * q.y + p1.y * q.x
  
#   return abs(center.x * a + center.y * b + c) / math.sqrt(a * a + b * b)

# def balgo(polygon, circle, color):
#   points = [v + polygon.pos for v in polygon.rotated]
  
#   for i in range(len(points)):
#     j = i + 1
#     if j >= len(points): j = 0
    
#     if dist(points[i], points[j], circle.pos) + 0.1 > circle.radius:
#       continue
    
#     K = points[j] - points[i]
#     P = points[i] - circle.pos
    
#     a = K.x * K.x + K.y * K.y
#     b = P.x * K.x + P.y * K.y
#     c = P.x * P.x + P.y * P.y - circle.radius * circle.radius
    
#     t1 = (-math.sqrt(b * b - a * c) - b) / a
#     t2 = ( math.sqrt(b * b - a * c) - b) / a
    
#     if 0 <= t1 and t1 <= 1 and 0 <= t2 and t2 <= 1:
#       p1 = points[i] + (points[j] - points[i]) * t1
#       p2 = points[i] + (points[j] - points[i]) * t2
      
#       drawLine(color, p1, p2)

# def algo(polygon, circle, color):
#   points = [v + polygon.pos for v in polygon.rotated]
  
#   ret_points = []
#   inside = [False] * len(points)
  
#   for i in range(len(inside)):
#     diff = points[i] - circle.pos
#     if diff.x * diff.x + diff.y * diff.y < circle.radius * circle.radius:
#       inside[i] = True
  
#   for i in range(len(points)):
#     if inside[i]:
#       for l in [-1, 1]:
#         j = i + l 
#         if j >= len(points): j = 0
#         if j < 0: j = len(points) - 1
        
#         diff = points[i] - circle.pos
        
#         if not inside[j]:
        
#           vec = (points[j] - points[i]).normalize()
          
#           a = vec.x * vec.x + vec.y * vec.y
#           b = vec.x * diff.x + vec.y * diff.y
#           c = vec.x * diff.y - vec.y * diff.x
          
#           t = (math.sqrt(circle.radius * circle.radius * a - c * c) - b) / a
          
#           s = points[i]
#           e = points[i] + vec * t
          
#           drawLine(color, s, e)
#           #pygame.draw.line(screen, color, s, e)
#           ret_points.append(points[i] + vec * t)
          
#         else:
#           s = points[i]
#           e = points[j]
          
#           drawLine(color, s, e)
#           #pygame.draw.line(screen, color, s, e)
  
#   return ret_points

#   # 선과 원이 만나는 경우를 생각 안함.
#   # 원과 원의 탐색


# velocity = Vector2D(0, 0)


# t = 0

# while True:
#   print(poly.pos)
  
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       pygame.quit()
#       sys.exit()
    
#     if event.type == pygame.KEYDOWN:
      
#       keys = pygame.key.get_pressed()
#       if keys[pygame.K_SPACE]:
#         circles.append(Circle(poly.pos.copy(), 1))
#       if keys[pygame.K_a]:
#         velocity = Vector2D(-1, -4)
#         circles.append(Circle(poly.pos.copy(), 1))
#       if keys[pygame.K_d]:
#         velocity = Vector2D(1, -4)
#         circles.append(Circle(poly.pos.copy(), 1))
  
#   speed = 1
#   keys = pygame.key.get_pressed()    

#   if keys[pygame.K_w]: poly.pos.y -= speed
#   if keys[pygame.K_s]: poly.pos.y += speed
#   if keys[pygame.K_a]: poly.pos.x -= speed
#   if keys[pygame.K_d]: poly.pos.x += speed
  
#   screen.fill((0, 0, 0))
   
#   qt = QuadTree(Rect(0, 0, 800 * 4, 600 * 4))
  
#   for wall in walls:
#     qt.insert(wall)
    
#   check_list = []
#   qt.search(poly.getRect(), check_list)
  
  
#   rqt = QuadTree(Rect(0, 0, 800 * 4, 600 * 4))
  
#   for r in red:
#     rqt.insert(r)
  
#   rcheck_list = []  
#   rqt.search(poly.getRect(), rcheck_list)
  
  
#   velocity = velocity + Vector2D(0, 0.1)
  
#   poly.pos = poly.pos + velocity
  
#   for check in check_list:
#     collid, mtv = SAT(poly, check)
    
#     if collid:
#       poly.pos = poly.pos + mtv
#       velocity = Vector2D(0, 0)
  
#   for check in rcheck_list:
#     collid, mtv = SAT(poly, check)
    
#     if collid:
#       exit(0)
#       break
      
  
#   for circle in circles:
#     circle.radius += 3
    
#   def chk(c):
#     return c.radius < 255
  
#   circles = list(filter(chk, circles))
  
#   circles.sort(key = lambda c: c.radius, reverse = True)
  
#   for circle in circles:
#     color = (255 - circle.radius, 255 - circle.radius, 255 - circle.radius)
    
#     circle_list = []
#     qt.search(circle.getRect(), circle_list)
  
  
#     for c in circle_list:
#       balgo(c, circle, color)
#       for p in algo(c, circle, color):
#         pygame.draw.circle(screen, color, (p - camera.padding()).toTuple(), 3)


#     color = (255 - circle.radius, 0, 0)

#     circle_list1 = []
#     rqt.search(circle.getRect(), circle_list1)

#     for c in circle_list1:
#       balgo(c, circle, color)
#       for p in algo(c, circle, color):
#         pygame.draw.circle(screen, color, (p - camera.padding()).toTuple(), 3)

#     circle.draw(screen, camera, (255 - circle.radius, 255 - circle.radius, 255 - circle.radius))

#   poly.draw(screen, camera, (0, 255, 0))
  
#   t += 0.2
  
#   v = math.sin(t)
  
#   pygame.display.flip()
#   pygame.time.Clock().tick(60)