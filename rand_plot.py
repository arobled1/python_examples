x = range(1,26)
y = []
for i in x:
    y.append(random.randint(65,75))
print "Below are the coordinates. Your random numbers are the y-coordinates."
print "x , y"
for i in x:
    print x[i-1], ",", y[i-1]
plt.xlim(0,26)
plt.ylim(60,80)
plt.plot(x, y, 'o', color='blue')
plt.xlabel("x")
plt.ylabel("y (Random Number)")
plt.savefig("points.pdf")
