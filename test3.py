#one more...
#for good measure
#if you cant tell im practicing vehicle dynamics equations

import numpy as np

def lat_tire_f(c_alpha, alpha):
    fyl = -2 * c_alpha * alpha 
    return fyl

# c_alpha = float(input("bruh moment 1?"))
# alpha = float(input("brhu m oment 2?"))
# answer = lat_tire_f(c_alpha, alpha)
# print(answer)

# #why is git being annoying

def fiala(c_alpha, alpha, mu, fz): #figaro figaro fiiiigarooooo
    if abs(alpha) < np.arctan((3*mu * fz)/c_alpha):
        fyf = -c_alpha * np.tan(np.radians(alpha)) + (c_alpha ** 2)/(3 * mu * fz) * abs(np.tan(np.radians(alpha))) * np.tan(np.radians(alpha))
    else:
        fyf = -mu * fz * np.sign(alpha)
    return fyf

ans = fiala(10,20,50,100)
print(ans)