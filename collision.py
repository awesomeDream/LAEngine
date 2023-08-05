from mathlib import Vector2D
from shape import Circle, Polygon

INF = 10000000000000

def SAT(s1, s2):
  if type(s1) == Polygon:
    if type(s2) == Polygon:
      return SAT_PP(s1, s2)
    else:
      return SAT_PC(s1, s2)
  else:
    if type(s2) == Polygon:
      return SAT_CP(s1, s2)
    else:
      return SAT_CC(s1, s2)

def SAT_CC(c1, c2):
  c3 = c1.pos - c2.pos
  d1 = c1.radius + c2.radius
  d2 = c3.magnitude()
  
  if d1 > d2:
    mtv = c3.normalize() * (d1 - d2)
    return (True, mtv)
  
  return (False, Vector2D(0, 0))

def polygon_normals(p, normals_in):
  for inext in range(len(p.rotated)):
    icurr = inext - 1 if inext else len(p.rotated) - 1   
    normals_in.append((p.rotated[icurr] - p.rotated[inext]).perpendicular().normalize())

def SAT_CP(p1, p2):
  v = SAT_PC(p2, p1)
  return (v[0], v[1] * -1)

def SAT_PC(p1, p2):
  normals = [(v + p1.pos - p2.pos).normalize() for v in p1.rotated]
  polygon_normals(p1, normals)
  
  mtv = Vector2D(INF, INF)
  mtv_mag = INF
  
  p1_points = [(p1.pos + q) for q in p1.rotated]
  
  for normal in normals:
    p1_min, p1_max = INF, -INF
    
    for p1_point in p1_points:
      proj = normal.dot(p1_point)
      if p1_max < proj: p1_max = proj
      if p1_min > proj: p1_min = proj
    
    proj = normal.dot(p2.pos)
    p2_min, p2_max = proj - p2.radius, proj + p2.radius
    
    c1 = p1_min < p2_max and p1_min > p2_min
    c2 = p2_min < p1_max and p2_min > p1_min

    if c1 or c2:
      m = p2_max - p1_min if c1 else p2_min - p1_max
      
      vec = normal * m
      vec_mag = vec.magnitude()
      
      if vec_mag < mtv_mag:
        mtv, mtv_mag = vec, vec_mag
        
    else:
      return (False, Vector2D(0, 0))
  
  return (True, mtv)

def SAT_PP(p1, p2):
  normals = []
  polygon_normals(p1, normals)
  polygon_normals(p2, normals)
  
  mtv = Vector2D(INF, INF)
  mtv_mag = INF
  
  p1_points = [(p1.pos + q) for q in p1.rotated]
  p2_points = [(p2.pos + q) for q in p2.rotated]
  
  for normal in normals:
    p1_min, p1_max = INF, -INF
      
    for p1_point in p1_points:
      proj = normal.dot(p1_point)
      if p1_max < proj: p1_max = proj
      if p1_min > proj: p1_min = proj
      
    p2_min, p2_max = INF, -INF
      
    for p2_point in p2_points:
      proj = normal.dot(p2_point)
      if p2_max < proj: p2_max = proj
      if p2_min > proj: p2_min = proj
      
    c1 = p1_min < p2_max and p1_min > p2_min
    c2 = p2_min < p1_max and p2_min > p1_min

    if c1 or c2:
      m = p2_max - p1_min if c1 else p2_min - p1_max
      
      vec = normal * m
      vec_mag = vec.magnitude()
      
      if vec_mag < mtv_mag:
        mtv, mtv_mag = vec, vec_mag
        
    else:
      return (False, Vector2D(0, 0))
  
  return (True, mtv)

def AABB(a, b):
  return (
    a.x < b.x + b.w and
    a.x + a.w > b.x and
    a.y < b.y + b.h and
    a.y + a.h > b.y
  )