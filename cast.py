from collisions import *
from  vector_math import *
from data import *
from ray_caster import *


def cast_ray(ray, sphere_list, color, light, eye_point, out): 
   l = find_intersection_points(sphere_list, ray)
   if l != []:
      spec_color = Color(0.0, 0.0, 0.0)                
      nearest_sphere = l[0][0]
      nearest_point = l[0][1]
      first_v = vector_from_to(ray.pt, nearest_point)
      nearest_dist = length_vector(first_v) 
      for (s, p) in l:
         dist = length_vector(vector_from_to(ray.pt, p))
         if dist < nearest_dist:
            nearest_dist = dist
            nearest_sphere = s
            nearest_point = p
      p_new = translate_point(nearest_point, (scale_vector(sphere_normal_at_point(nearest_sphere, nearest_point), 0.01)))
      n = sphere_normal_at_point(nearest_sphere, nearest_point)
      l_dir = normalize_vector(vector_from_to(p_new, light.pt))
      check_light =  dot_vector(n, l_dir) 
      scale_n = scale_vector(n, (2 * check_light)) 
      ref_vector = difference_vector(l_dir, scale_n)
      v_dir = normalize_vector(vector_from_to(eye_point, p_new))
      spec_intensity = dot_vector(ref_vector, v_dir)
      if spec_intensity > 0:
         r = light.color.r * nearest_sphere.finish.specular * (spec_intensity**(1.0/nearest_sphere.finish.roughness)) 
         g = light.color.g * nearest_sphere.finish.specular * (spec_intensity**(1.0/nearest_sphere.finish.roughness)) 
         b = light.color.b * nearest_sphere.finish.specular * (spec_intensity**(1.0/nearest_sphere.finish.roughness)) 
         spec_color = Color(r,g,b)
      if check_light > 0 and check_ray(sphere_list, p_new, light, l_dir):
         light = light_product(check_light, light.color, nearest_sphere.color, nearest_sphere.finish.diffuse) 
         convert_color(nearest_sphere.color, nearest_sphere.finish.ambient, color, light, spec_color, out)
      else:
         convert_color(nearest_sphere.color, nearest_sphere.finish.ambient, color, Color(0.0, 0.0, 0.0), spec_color, out)
   else:
      out.write('255 255 255\n')    

def check_ray(sphere_list, p_new, light, l_dir):   
   ray_to_light = data.Ray(p_new, l_dir)
   light_tuples = find_intersection_points(sphere_list, ray_to_light)
   dist_light = length_vector(vector_from_to(p_new, light.pt))
   for (s,p) in light_tuples:
      if length_vector(vector_from_to(p_new, p)) < dist_light:  
         return False
   return True

def light_product(check_light, l_color, s_color, diffuse):
   r = l_color.r * s_color.r * check_light * diffuse
   g = l_color.g * s_color.g * check_light * diffuse
   b = l_color.b * s_color.b * check_light * diffuse
   return Color(r,g,b)

def convert_color(c, a, color, light, spec_color, out):
   r = min((c.r * a * color.r + light.r + spec_color.r), 1.0)
   final_r = int(r*255)
   g = min((c.g * a * color.g + light.g + spec_color.g), 1.0)
   final_g = int(g*255)
   b = min((c.b * a * color.b + light.b + spec_color.b), 1.0)
   final_b = int(b*255)
   final = '' + str(final_r) + ' ' + str(final_g) + ' ' + str(final_b)
   out.write(final + '\n')
   
 
def cast_all_rays(min_x, max_x, min_y, max_y, width, heigth, eye_point, sphere_list, color, light, out):
   x_pix = (max_x - min_x) / width
   y_pix = (max_y - min_y) / heigth
   for y in range(0, heigth):
      for x in range(0, width):
         to_point =  data.Point( (min_x + (x_pix *x)), (max_y - (y_pix * y)), 0)
         vector = vector_from_to(eye_point, to_point)
         ray = data.Ray(eye_point, vector)
         cast_ray(ray, sphere_list, color, light, eye_point, out)

