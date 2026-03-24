#this is another thing i will do now.

#function that simulates car's position over time using kinematic single track model.
#start at 0,0 and update x,y over small time steps.

import numpy as np

#vehicle parameters
vehicle = {
    "u" : 30,
    "delta" : np.radians(30),
    "psi" : np.radians(15),
    "l" : 3,
    "lr" : 1.75,
    "m" : 1500
}

#beta. sideslip angle
beta = np.arctan((vehicle["lr"]/vehicle["l"]) * np.tan(vehicle["delta"]))
print(beta)