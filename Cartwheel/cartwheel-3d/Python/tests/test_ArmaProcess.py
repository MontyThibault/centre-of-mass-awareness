import unittest
from ArmaProcess import ArmaProcess


import time

class ArmaProcessTestCase(unittest.TestCase):
    
    def testGenSamples(self):
        
        
        params = [3.75162180e-04, 1.70361201e+00, -7.30441228e-01, -6.22795336e-01, 3.05330848e-01]
        
        ap = ArmaProcess(params[0], params[1:3], params[3:5], 100)
        
        print(ap.generate_n(20))
        
       
        
        for _ in range(3):
            
            time.sleep(0.04)
            
            print(ap.generate_frame())