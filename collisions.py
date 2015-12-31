from data import *
from  vector_math import *
import math

def sphere_intersection_point(ray, sphere):   
   a = dot_vector(ray.dir, ray.dir)

   b_vector = difference_point(ray.pt, sphere.center)
   b_scaled = scale_vector(b_vector, 2)
   b = dot_vector(b_scaled, ray.dir)

   c_vector = difference_point(ray.pt, sphere.center)
   c_dot = dot_vector(c_vector, c_vector)
   c = (c_dot) - (sphere.radius**2)

   d = (b**2) - (4*a*c)
   if d < 0:
      return None
 
   sol1 = ((-b - math.sqrt(d)) / (2*a))
   sol2 = ((-b + math.sqrt(d)) / (2*a))
   
   if (sol1 >= 0 and sol2 >= 0):
      if sol1 > sol2:
         t = sol2
      else:
         t = sol1
   elif (sol1 < 0 and sol2 < 0):
      return None
   elif (sol1 < 0 and sol2 >= 0):
      t = sol2
   elif (sol1 >= 0 and sol2 < 0):
      t = sol1   

   t_scaled = scale_vector(ray.dir, t)
   final = translate_point(ray.pt, t_scaled)
   return final  

def find_intersection_points(sphere_list, ray):
   intersected_spheres = [s for s in sphere_list if sphere_intersection_point(ray, s) != None]   
   tuple_list = [(s, sphere_intersection_point(ray, s)) for s in intersected_spheres]
   return tuple_list

def sphere_normal_at_point(sphere, point):
   vector = vector_from_to(sphere.center, point)
   normal = normalize_vector(vector)
   return normal
