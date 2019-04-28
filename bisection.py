import math

def func(xin):
    return 3*xin - math.exp(xin)

def bisection(a, b, tol):
    i = 0
    counter = 0
    while i == 0:
        counter = counter + 1
        c = (a + b)/2.0
        fa = func(a)
        fb = func(b)
        fc = func(c)
        if fa == 0:
            print "Your value for left interval turned out to be the root of the function"
        elif fb == 0:
            print "Your value for right interval turned out to be the root of the function"
        elif fc == 0 or (b-a)/2.0 < tol:
            i = 1
        if fa*fc > 0:
            a = c
        else:
            b = c
    return c, counter

print """We're gonna find the root for
f(x) = 3x - e^x
on [1,2] with a tolerance of 10^-6."""
a = 1.0
b = 2.0
print "\nUsing the bisection method,"
tol = 10**-6
root, counter = bisection(a, b, tol)
print "The calculated root is: ", root
print "# of iterations: ", counter
