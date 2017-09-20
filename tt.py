
"""
Created on Wed Sep 20 19:20:00 2017

@author: happytech
"""

import numpy as np

def f(x,y):
    return (x+1)*(y+1)

tt = np.fromfunction(f,(12,12),dtype=int)
print(tt)

