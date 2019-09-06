 #===============================================================================
# Description:
# Generates a list of 25 numbers and plots each number.
# Coordinates for plotting are made by making each random number the y
# coordinate and the order in which the number is generated the x coordinate.
#===============================================================================
# Author: Alan Robledo
#===============================================================================
import random
import matplotlib.pyplot as plt
x = range(1,26)
y = []
for i in x:
    y.append(random.randint(65,75))
print("Below are the coordinates. Your random numbers are the y-coordinates.")
print("x , y")
for i in x:
    print(x[i-1], ",", y[i-1])
plt.xlim(0,26)
plt.ylim(60,80)
plt.plot(x, y, 'o', color='blue')
plt.xlabel("x")
plt.ylabel("y (Random Number)")
plt.savefig("points.pdf")
