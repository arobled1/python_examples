import numpy as np

max_iter = 20  # Max number of iterations (set by user)
tol = 10**-3   # Tolerance (set by user)

# Example matrix A:
# -4 14 0
# -5 13 0
# -1 0  2
mat = np.array([[-4,14,0],[-5,13,0],[-1,0,2]])
# Example column vector:
# [1 1 1]^T
init_vec = np.array([1, 1, 1])
xp = abs(max(init_vec, key=abs))  # Finding l-infinity norm of initial vector x
# Rescaling the initial vector to prevent from blowing up
init_vec = init_vec / xp

i = 0
while i < max_iter:
    i += 1
    # Matrix multiplying A with the initial vector x
    y = np.matmul(mat, init_vec)
    # Finding the l-infinity norm of the result from Ax.
    # This serves as the dominant eigenvalue.
    eig_val = abs(max(y, key=abs))
    error = abs(max(init_vec - (y/eig_val), key=abs))
    init_vec = y / eig_val
    print("Iteration #:", i)
    print("Eigenvalue", eig_val)
    print("")
    if error < tol:
        print("Success!")
        print("Dominant eigenvalue is:", eig_val)
        print("Dominant eigenvector is:", init_vec)
        i = max_iter + 1
    if i == max_iter:
        print("Exceeded max iterations. Try a new initial vector.")
