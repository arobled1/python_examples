#=============================================================================80
# Description:
# Modeling a monoatomic ideal gas in a box with walls at x = 0 and x = 1 at a
# height of y = 10.
# Box will have no top but the program will stop when the atom leaves the box.
# Model contains only one atom for now.
# Will soon update for an arbitrary number of atoms.
#===============================================================================
# Author: Alan Robledo
# Date modified: May 29, 2019
#===============================================================================

import random as rn
import numpy as np
import matplotlib.pyplot as plt

# Initial positions
x = rn.random()
y = rn.random() * 10
# Initial velocity as a random number between 0.1 and 0.03.
# Velocities are arbitrarily chosen.
vel = rn.random()
vel = vel*(0.10 - 0.03) + 0.03
# Random number between 0 and 2*pi
angle = rn.random() * 2 * np.pi
vel_x = vel * np.cos(angle)
vel_y = vel * np.sin(angle)
# Initial time
t = 0
dt = 2

xs = []
ys = []
while t == 0 or y < 10:
    xs.append(x)
    ys.append(y)
    x = x + vel_x * dt
    y = y + vel_y * dt
    t = t + dt
    # If the atom goes past the ground
    if y < 0:
        vel_y = - vel_y
        y = 0
    # If the atom goes past the left wall
    if x < 0:
        vel_x = -vel_x
        x = 0
    # If the atom goes past the right wall
    if x > 1:
        vel_x = -vel_x
        x = 1
plt.xlim(0,1)
plt.ylim(0,10)
plt.plot(xs,ys,'o-')
plt.savefig("box%s.pdf" % i)
plt.clf()
