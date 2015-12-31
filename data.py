from utility import *
class Point:
   """ a model for a 3d point
   Attributes:
      x, int
      y, int
      z, int """
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z
   def __eq__(self, other):
      return(epsilon_equal(self.x, other.x) and
             epsilon_equal(self.y, other.y) and
             epsilon_equal(self.z, other.z)) 

class Vector:
   def __init__(self, x, y ,z):
      self.x = x
      self.y = y
      self.z = z
   def __eq__(self, other): 
      return(epsilon_equal(self.x, other.x) and
             epsilon_equal(self.y, other.y) and
             epsilon_equal(self.z, other.z))   

class Ray:
   """ a model of a ray used to generate images
   Attributes: 
      pt, Point object
      dir, Vector object """
   def __init__(self, pt, dir):
      self.pt = pt
      self.dir = dir
   def __eq__(self, other):
      return(epsilon_equal(self.pt.x, other.pt.x) and
             epsilon_equal(self.pt.y, other.pt.y) and
             epsilon_equal(self.pt.z, other.pt.z) and
             epsilon_equal(self.dir.x, other.dir.x) and
             epsilon_equal(self.dir.y, other.dir.y) and
             epsilon_equal(self.dir.z, other.dir.z))

class Color:
   def __init__(self, r, g, b):
      self.r = r
      self.g = g
      self.b = b
   def __eq__(self, other):
      return(epsilon_equal(self.r, other.r) and
             epsilon_equal(self.g, other.g) and
             epsilon_equal(self.b, other.b))

class Sphere:
   """ a model of a sphere
   Attributes:
      center, Point object
      radius, float """
   def __init__(self, center, radius, color, finish):
      self.center = center
      self.radius = radius
      self.color = color
      self.finish = finish 
   def __eq__(self, other):
      return(epsilon_equal(self.center.x, other.center.x) and
             epsilon_equal(self.center.y, other.center.y) and
             epsilon_equal(self.center.z, other.center.z) and
             epsilon_equal(self.radius, other.radius) and
             epsilon_equal(self.color.r, other.color.r) and
             epsilon_equal(self.color.g, other.color.g) and
             epsilon_equal(self.color.b, other.color.b) and
             epsilon_equal(self.finish.ambient, other.finish.ambient) and
             epsilon_equal(self.finish.diffuse, other.finish.diffuse))

class Finish:
   def __init__(self, ambient, diffuse, specular, roughness):
      self.ambient = ambient
      self.diffuse = diffuse
      self.specular = specular
      self.roughness = roughness
   def __eq__(self, other):
      return(epsilon_equal(self.ambient, other.ambient) and
             epsilon_equal(self.diffuse, other.diffuse) and
             epsilon_equal(self.specular, other.specular) and
             epsilon_equal(self.roughness, other.roughness))

class Light:
   def __init__(self, pt, color):
      self.pt = pt
      self.color = color
   def __eq__(self, other):
      return(epsilon_equal(self.pt, other.pt) and
             epsilon_equal(self.color, other.color))







