#===============================================================================
# Finds the roots of ax**2 + bx + c == 0 for any arbitrary coefficients that are
# specified by the user.
# First, a function is defined to solve the quadratic equation.
# Then the user is asked what they want the coefficients to be.
#===============================================================================
# Author: Alan Robledo
#===============================================================================
# To test for 2 real roots use:    a = 1, b = 6, c = 3
#             Output should be:    x1 = (-0.550510257217+0j)
#                                  x2 = (-5.44948974278+0j)
# To test for 1 real root use:     a = -4, b = 12, c = -9
#             Output should be:    x1 = (1.5+0j)
#                                  x2 = (1.5+0j)
# To test for 2 complex roots use: a = 1, b = 2, c = 3
#             Output should be:    x1 = (-1+1.41421356237j)
#                                  x2 = (-1-1.41421356237j)
#===============================================================================
# Notes:
# In order for numpy to compute the square root of a negative number, the
# argument must be in the form of a complex number where j = sqrt(-1).
#===============================================================================
def solve_quad(a, b, c):
    solns = []
    discrim = b**2 - 4*a*c
    solns.append( (-b + np.sqrt(discrim + 0j)) / (2*a) )
    solns.append( (-b - np.sqrt(discrim + 0j)) / (2*a) )
    return solns

a = float(raw_input("What is a? "))
b = float(raw_input("What is b? "))
c = float(raw_input("What is c? "))
solutions = solve_quad(a, b, c)
if solutions[0] == solutions[1]:
    print "Uh oh, there's only one root."
    print 'x1 = {0}\nx2 = {1}'.format(*solutions)
else:
    print "Here are your solutions:"
    print 'x1 = {0}\nx2 = {1}'.format(*solutions)
