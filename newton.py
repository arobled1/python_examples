import math

def func(xin):
    return xin - 2**(-xin)

def func_prime(xin):
    return 1 + math.log(2)*2**(-xin)

def newton(a, tol):
        i = 0
        counter = 0
        while i == 0:
            counter = counter + 1
            fa = func(a)
            fa_prime = func_prime(a)
            a_new = a - fa / fa_prime
            if abs(a_new - a) < tol:
                i = 1
            else:
                a = a_new
        return a, counter

print """We're gonna find the root for
f(x) = x - 2^-x
with an initial solution of p_o = 2 and a tolerance of 10**-5."""
print "\nUsing newton's method,"
a = 2
tol = 10**-5
root, counter = newton(a, tol)
print "The calculated root is: ", root
print "# of iterations: ", counter
