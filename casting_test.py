
from cast import *

eye_point = Point(0.0,0.0,-14.0)
sphere_list = [Sphere(Point(1.0, 1.0, 0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(Color(0.2, 0.2, 0.2), 0.4, 0.5, 0.05)), 
               Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(Color(0.4, 0.4, 0.4), 0.4, 0.5, 0.05))]
light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))

print 'P3'
print '1024 768'
print '255' 
outfile = open('image.ppm', 'w')
outfile.write(cast_all_rays(-10.0, 10.0, -7.5, 7.5, 1024, 768, eye_point, sphere_list, Color(1.0, 1.0, 1.0), light)/n)
