import numpy as np

max_iter = 20
tol = 10**-3

mat = np.array([[-4,14,0],[-5,13,0],[-1,0,2]])
init_vec = np.array([1, 1, 1])

xp = abs(max(init_vec, key=abs))
init_vec = init_vec / xp

i = 0
while i < max_iter:
    i += 1
    y = np.matmul(mat, init_vec)
    yp = abs(max(y, key=abs))
    mu = yp
    error = abs(max(init_vec - (y/yp), key=abs))
    init_vec = y/yp
    print("Iteration #:", i)
    print("Eigenvalue", mu)
    print("")
    if error < tol:
        print("Success!")
        print("Dominant eigenvalue is:", mu)
        print("Dominant eigenvector is:", init_vec)
        i = max_iter + 1
    if i == max_iter:
        print("Exceeded max iterations. Try a new initial vector.")
