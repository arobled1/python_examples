import math

def func(xin):
    return xin - 2**(-xin)

def false(a0, a1, tol):
    fa0 = func(a0)
    fa1 = func(a1)
    i = 0
    counter = 0
    while i == 0:
        counter = counter + 1
        a2 = a1 - (fa1 * (a1 - a0) ) / (fa1 - fa0)
        if abs(a2 - a1) < tol:
            i = 1
        else:
            fa2 = func(a2)
            if fa2*fa1 < 0:
                a0 = a1
                fa0 = fa1
            a1 = a2
            fa1 = fa2
    return a2, counter


print """We're gonna find the root for
f(x) = x - 2^-x
with an initial solution of p_o = 0 and p_1 = 2
and a tolerance of 10**-5."""
a0 = 0.0
a1 = 2.0
print "\nUsing the false position method,"
tol = 10**-5
root, counter = false(a0, a1, tol)
print "The calculated root is: ", root
print "# of iterations: ", counter
