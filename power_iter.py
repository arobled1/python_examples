#=============================================================================80
# Description:
# Finds the dominant eigenvalue and associated eigenvector of a square matrix
# A of size NxN using the Power Method, aka Power Iteration.
# The user must specify an intial vector to represent the dominant eigenvector.
# The initial vector is usually chosen to be an array of ones or some unit
# vector (e.g. [1 0 0]).
#===============================================================================
# Author: Alan Robledo
# Date: 9/26/19
#===============================================================================
# Output:
# Iteration #: 13
# Dominant eigenvalue is: 6.000418585182082
# Dominant eigenvector is: [ 1.          0.71430066 -0.24994761]
#===============================================================================
import numpy as np

def power_iter(max_iterations, tolerance, matrix, vec):
    # Finding l-infinity norm of initial vector x
    xp = abs(max(vec, key=abs))
    # Rescaling the initial vector to prevent from blowing up
    vec = vec / xp
    i = 0
    while i < max_iterations:
        i += 1
        # Matrix multiplying A with the initial vector x
        y = np.matmul(matrix, vec)
        # Finding the l-infinity norm of the result from Ax.
        # This serves as the dominant eigenvalue.
        eig_val = abs(max(y, key=abs))
        error = abs(max(vec - (y/eig_val), key=abs))
        vec = y / eig_val
        print("Iteration #:", i)
        print("Eigenvalue", eig_val)
        print("")
        if error < tolerance:
            print("Success!")
            i = max_iterations + 1
        if i == max_iterations:
            print("Exceeded max iterations. Try a new initial vector.")
    return eig_val, vec
    
# Max number of iterations (set by user)
max_iter = 20
# Tolerance (set by user)
tol = 10**-4

# Example matrix A:
# -4 14 0
# -5 13 0
# -1 0  2
mat = np.array([[-4,14,0],[-5,13,0],[-1,0,2]])

# Example column vector:
# [1 1 1]^T
init_vec = np.array([1, 1, 1])
eig_val, eig_vec = power_iter(max_iter, tol, mat, init_vec)
print("Dominant eigenvalue is:", eig_val)
print("Dominant eigenvector is:", eig_vec)
