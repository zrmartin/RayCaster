import data
from math import sqrt

def scale_vector(vector, scalar):
   x = vector.x * scalar
   y = vector.y * scalar
   z = vector.z * scalar
   return data.Vector(x, y, z)

def dot_vector(vector1, vector2):
   x = vector1.x * vector2.x
   y = vector1.y * vector2.y
   z = vector1.z * vector2.z
   return (x + y + z)
  
def length_vector(vector):
   x = vector.x**2
   y = vector.y**2
   z = vector.z**2
   return sqrt(x + y + z)

def normalize_vector(vector):
   l = length_vector(vector)
   return scale_vector(vector, (1.0/l))

def difference_point(point1, point2):
   x = point1.x - point2.x
   y = point1.y - point2.y
   z = point1.z - point2.z
   return(data.Vector(x, y, z)) 

def difference_vector(vector1, vector2):
   x = vector1.x - vector2.x
   y = vector1.y - vector2.y
   z = vector1.z - vector2.z
   return(data.Vector(x, y, z))

def translate_point(point, vector):
   x = point.x + vector.x
   y = point.y + vector.y
   z = point.z + vector.z 
   return(data.Point(x, y ,z))

def vector_from_to(from_point, to_point):
   return difference_point(to_point, from_point)
  

	
