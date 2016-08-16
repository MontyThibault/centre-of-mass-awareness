from collections import deque
from random import gauss


class ArmaProcess(object):
    
    def __init__(self, c, ar, ma):
        
        self.c = c
        self.ar = ar
        self.ma = ma
        
        self.past_val = deque([0] * len(ar), len(ar))
        self.past_rnd = deque([0] * len(ma), len(ma))

        
        
    def generate(self):
        
        rnd = gauss(0, 1)
        
        ma_term = sum([a * b for a, b in zip(self.ma, self.past_rnd)])
        ar_term = sum([a * b for a, b in zip(self.ar, self.past_val)])
        
        val = self.c + rnd + ma_term + ar_term
        
        self.past_val.appendleft(val)
        self.past_rnd.appendleft(rnd)
        
        return val
    
    
    def generate_n(self, n):
        
        return [self.generate() for _ in range(n)]