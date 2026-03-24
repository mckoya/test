#this is me testing that everything is on my computer

#lets do this thing

print("hello world")

#okaaaay lets go

import numpy as np

vehicle = { #i am making these all up fyi
    "l" : 3,
    "lf" : 1.8,
    "lr" : 1.2,
    "m" : 1000,
    "psi" : 30,
    "u" : 40,
    "v" : 5,
    "r" : 10,
}

def ddx_longvelocity(f_xr, f_xf, f_yr, f_yf, fxother) :
    #dyanmic single track, outputs udot, vdot, rdot
    udot = (1/vehicle["m"]) * (f_xr - f_yf * (np.sin(vehicle["psi"])) + f_xf*np.cos(vehicle["psi"]) + fxother) + (vehicle["v"] * vehicle["r"])
    vdot = (1/vehicle["m"]) * (f_yr + f_yf * (np.cos(vehicle["psi"])) + f_xf*np.sin(vehicle["psi"])) - (vehicle["u"] * vehicle["r"])
    rdot = 