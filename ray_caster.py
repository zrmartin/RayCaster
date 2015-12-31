from cast import *
from data import *
from sys import *
from commandline import *

def main():
   
   s_list = check_spheres()         
   
   eye = check_eye()
  
   view = check_view()
   min_x = view[0]
   max_x = view[1]
   min_y = view[2]
   max_y = view[3]
   width = view[4]
   height = view[5]

   light = check_light()
   l = light[0]
   c = light[1]

   a_c = check_ambient()   
  
   out = open("image.ppm", "w")
   out.write('P3\n')
   out.write(str(width) + ' ' +  str(height)+ '\n')
   out.write('255\n')
   cast_all_rays(min_x, max_x, min_y, max_y, width, height, Point(eye.x, eye.y, eye.z), s_list, Color(a_c.r, a_c.g, a_c.b), Light(Point(l.x, l.y, l.z), Color(c.r, c.g, c.b)), out)
  
   
   
if __name__ == '__main__':
   main()
