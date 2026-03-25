#one more...
#for good measure
#if you cant tell im practicing vehicle dynamics equations

import numpy as np

def lat_tire_f(c_alpha, alpha):
    fyl = -2 * c_alpha * alpha 
    return fyl

c_alpha = int(input("bruh moment 1?"))
alpha = int(input("brhu m oment 2?"))
answer = lat_tire_f(c_alpha, alpha)
print(answer)