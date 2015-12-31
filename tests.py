import unittest
from commandline import *
class Tests(unittest.TestCase):
   
   def test_check_in_file(self): 
      self.assertEqual(check_in_file(['commandline.py', 'junk.txt']), True)        
   def test_check_in_file(self):
      self.assertEqual(check_in_file(['commandline.py']), False)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()


