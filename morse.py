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
#
#===============================================================================

xbound = 50
ngrid = 2000
dx = (2.0 * xbound) / (ngrid - 1)
x_grid = [-xbound + i * dx for i in xrange(ngrid)]
