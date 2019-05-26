#=============================================================================80
# Description:
# Computing the hamiltonian for a 1D morse oscillator.
#===============================================================================
# Author: Alan Robledo
# Date modified: May 26, 2019
#===============================================================================
# Variables:
# xbound = sets the bound in the positive and negative direction
# ngrid = number of grid points
# dx = dist. between points (Remember: for every ngrid points, there
#       are ngrid - 1 dx)
# d_well = depth of the morse potential well
# mass = reduced mass
#===============================================================================
import numpy as np
from numpy import linalg as la

def generate_grid(xmin, xmax, ngrid):
    dx = (xmax - xmin) / (ngrid - 1)
    x_grid = [xmin + i * dx for i in xrange(ngrid)]
    return dx, x_grid

def get_kinetic(ngrid, dx):
    ke_matrix = np.zeros((ngrid, ngrid))
    ke_matrix[0][0] = -2
    ke_matrix[1][0] = 1
    ke_matrix[ngrid - 1][ngrid - 1] = -2
    ke_matrix[ngrid - 2][ngrid - 1] = 1
    for i in xrange(1, ngrid - 1):
        ke_matrix[i - 1][i] = 1
        ke_matrix[i][i] = -2
        ke_matrix[i + 1][i] = 1
    return -(hbar**2 / (2.0 * mass)) * dx**-2 * ke_matrix

def get_potential(ngrid):
    pe_matrix = np.zeros((ngrid, ngrid))
    for i in xrange(ngrid):
        pe_matrix[i][i] = d_well * (np.exp(-omegax * x_grid[i]) - 1)**2
    return pe_matrix

d_well = 2
hbar = 1
mass = 1
omegax = 1

xmin = -2.0
xmax = 12.0
ngrid = 300
dx, x_grid = generate_grid(xmin, xmax, ngrid)
ke_matrix = get_kinetic(ngrid, dx)
pe_matrix = get_potential(ngrid)
hamiltonian = ke_matrix + pe_matrix
eig_val, eig_vec = la.eig(hamiltonian)
print eig_val
