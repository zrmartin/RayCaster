from sys import *
from cast import *
from data import*

def check_spheres():
   try:
      in_file = open(argv[1], 'r')
      num = 0
      spheres = []
      for line in in_file:
         l = line.split()
         if len(l) == 11:
            try:
               new = [float(i) for i in l]
               x = new[0]
               y = new[1]
               z = new[2]
               rad = new[3]
               r = new[4]
               g = new[5]
               b = new[6]
               ambient = new[7]
               diffuse = new[8]
               specular = new[9]
               roughness = new[10]
               spheres.append(Sphere(Point(x, y ,z), rad, Color(r, g ,b), Finish(ambient, diffuse, specular, roughness))) 
               num += 1
            except:
               print 'malformed sphere on line', num, '....skipping'
               num += 1
         else:
            print 'malformed sphere on line', num, '....skipping'
            num += 1
      return spheres
   except:
      print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
      exit()

def check_eye():
   if "-eye" in argv:
      try:
         eye = argv.index('-eye')
         x = float(argv[eye + 1])
         y = float(argv[eye + 2])
         z = float(argv[eye + 3])
         p = Point(x, y, z)
         return p
      except:
         p = Point(0.0, 0.0, -14.0)
         return p
   else:
      p = Point(0.0, 0.0, -14.0)
      return p


def check_view():
   min_x = -10.0
   max_x = 10.0
   min_y = -7.5
   max_y = 7.5
   width = 1024
   height = 768
   if "-view" in argv:
      try:
         view = argv.index('-view')
         min_x = float(argv[view + 1])
         max_x = float(argv[view + 2])
         min_y = float(argv[view + 3])
         max_y = float(argv[view + 4])
         width = int(argv[view + 5])
         height = int(argv[view + 6])
         return (min_x, max_x, min_y, max_y, width, height)
      except:
         return (min_x, max_x, min_y, max_y, width, height)
   else:
      return (min_x, max_x, min_y, max_y, width, height)

def check_light():
   if "-light" in argv:
      try:
         light = argv.index('-light')
         x = float(argv[light + 1])
         y = float(argv[light + 2])
         z = float(argv[light + 3])
         r = float(argv[light + 4])
         g = float(argv[light + 5])
         b = float(argv[light + 6])
         p = Point(x, y, z)
         c = Color(r, g, b)
         return (p, c)
      except:
         p = Point(-100.0, 100.0, -100.0)
         c = Color(1.5, 1.5, 1.5)
         return (p, c)
   else:
      p = Point(-100.0, 100.0, -100.0)
      c = Color(1.5, 1.5, 1.5)
      return (p, c)

def check_ambient():
   if "-ambient" in argv:
      try:
         ambient = argv.index('-ambient')
         r = float(argv[ambient + 1])
         g = float(argv[ambient + 2])
         b = float(argv[ambient + 3])
         return Color(r, g, b)
      except:
         return Color(1.0, 1.0, 1.0)
   else:
      return Color(1.0, 1.0, 1.0)
   
