#this is another thing i will do now.

#function that simulates car's position over time using kinematic single track model.
#start at 0,0 and update x,y over small time steps.

import numpy as np

#vehicle parameters
vehicle = {
    "u" : 30,
    "v" : 10,
    "delta" : np.radians(30),
    "psi" : np.radians(15),
    "l" : 3,
    "lr" : 1.75,
    "m" : 1500
}

#beta. sideslip angle
beta = np.arctan((vehicle["lr"]/vehicle["l"]) * np.tan(vehicle["delta"]))

#declare starting shit
X = 0
Y = 0
psi = 0
dt = 0.05

#these are the derivatives used in the euler new = old + derivative * dt
Xdot = vehicle["u"] * np.cos(vehicle["psi"] + vehicle["delta"])
Ydot = vehicle["v"] * np.sin(vehicle["psi"] + vehicle["delta"])
psidot = (vehicle["u"]/vehicle["lr"]) * np.sin(beta)
