#=============================================================================80
# Description:
# Computing the hamiltonian for a morse oscillator on a 1D grid.
#===============================================================================
# Author: Alan Robledo
# Date modified: May 25, 2019
#===============================================================================
# Variables:
# xbound = sets the bound in the positive and negative direction
# ngrid = number of grid points
# dx = dist. between points (Remember: for every ngrid points, there
#       are ngrid - 1 dx)
#===============================================================================
import numpy as np

def generate_grid(xbound, ngrid):
    dx = (2.0 * xbound) / (ngrid - 1)
    x_grid = [-xbound + i * dx for i in xrange(ngrid)]
    return dx, x_grid

def get_kinetic(ngrid):
    ke_matrix = np.zeros((ngrid, ngrid))
    ke_matrix[0][0] = -2
    ke_matrix[1][0] = 1
    ke_matrix[ngrid - 1][ngrid - 1] = -2
    ke_matrix[ngrid - 2][ngrid - 1] = 1
    for i in xrange(1, ngrid - 1):
        ke_matrix[i - 1][i] = 1
        ke_matrix[i][i] = -2
        ke_matrix[i + 1][i] = 1
    return ke_matrix

def get_potential(ngrid):
    pe_matrix = np.zeros((ngrid, ngrid))
    for i in xrange(ngrid):
        pe_matrix[i][i] = (np.exp(-x_grid[i]) - 1)**2
    return pe_matrix

xbound = 10
ngrid = 2000
dx, x_grid = generate_grid(xbound, ngrid)

ke_matrix = get_kinetic(ngrid)
pe_matrix = get_potential(ngrid)
