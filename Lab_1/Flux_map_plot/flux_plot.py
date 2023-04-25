import numpy as np
import matplotlib.pyplot as plt

# Author: Joanna P. Morgan
# Date May 25th 2023
# Purpose: Generating flux contour plots for Nuclear Reactor Lab 1

# importing data
data = np.genfromtxt("flux.csv",delimiter=",", dtype=float)

#getting rid of the text on the top and right
data = data[1:,:]
data = data[:,1:]

# data is now orginized into cols of y, z, flux, error

# generating figure
fig = plt.figure()

f = plt.tricontourf(data[:,0], data[:,1], data[:,2], cmap='viridis')

plt.xlabel('y [cm]')
plt.ylabel('z [cm]')
cbar = fig.colorbar(f)
cbar.ax.set_ylabel(r'x-averaged Scalar Flux [$\phi$]')
cbar.formatter.set_powerlimits((0, 0))

#plt.show()
plt.savefig('flux_map.png')
