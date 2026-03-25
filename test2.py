#this is another thing i will do now.

#function that simulates car's position over time using kinematic single track model.
#start at 0,0 and update x,y over small time steps.

import numpy as np
import matplotlib.pyplot as plt

#vehicle parameters
vehicle = {
    "u" : 30,
    "v" : 10,
    "delta" : np.radians(30), #steering angle
    "psi" : np.radians(15), #heading relative to whatever you decide the x axis to be
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

Xlist = []
Ylist = []

for i in range(50):
    #these are the derivatives used in the euler new = old + derivative * dt
    Xdot = vehicle["u"] * np.cos(vehicle["psi"] + beta)
    Ydot = vehicle["v"] * np.sin(vehicle["psi"] + beta)
    #psidot = (vehicle["u"]/vehicle["lr"]) * np.sin(beta)
    X = X + Xdot * dt
    Y = Y + Ydot * dt
    #psi = psi + psidot * dt
    Xlist.append(X)
    Ylist.append(Y)


#print(X,Y)
#print(Xlist)
#print(Ylist)

#plot, turning x into lists
plt.plot(Xlist, Ylist, "r*")
plt.xlabel("x position")
plt.ylabel("y position")
plt.title("the")
plt.show()