from collections import deque
from random import gauss
from time import time

class ArmaProcess(object):
    
    def __init__(self, c, ar, ma, fps):
        """
        
        c - Constant
        ar - Autoregression coefficients
        ma - Moving Average coefficients
        fps - the framerate of the dataset on which the model was trained
        
        """
        
        self.c = c
        self.ar = ar
        self.ma = ma
        
        self.past_val = deque([0] * len(ar), len(ar))
        self.past_rnd = deque([0] * len(ma), len(ma))
        
        self.fps = fps
        self.last_time = time()
        
        
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
    
    
    def generate_frame(self):
        
        now = time()
        
        num_seconds = now - self.last_time
        num_samples = int(num_seconds * self.fps)
        
        
        if num_samples == 0:
            return 0
        
        
        samples = self.generate_n(num_samples)
        averaged_sample = sum(samples) / num_samples
        
        
        self.last_time = now
        return averaged_sample
        
        