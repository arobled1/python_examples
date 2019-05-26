#=============================================================================80
# Description:
# Computing the hamiltonian for a morse oscillator on a 1D grid. 
#===============================================================================
# Author: Alan Robledo
# Date modified: May 25, 2019
#===============================================================================
# Variables:
# 'xbound' = 
#===============================================================================
xbound = 50
ngrid = 2000
dx = (2.0 * xbound) / (ngrid - 1)
x0 = -(ngrid + 1) * dx * 0.5
x_grid = [-xbound + i * dx for i in xrange(1, ngrid)]
