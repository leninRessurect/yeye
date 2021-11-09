import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#Defining constants
L = 2*np.pi
N = 20
K = 2

#Defining mesh, discretizing spacial dimension
xvector = np.linspace(0,L,N)
delx = xvector[2] - xvector[1]

#Discretizing in time and defining stability criterion
delt = 0.5*((delx)**2/2*K)
tvector = np.arange(0, L, delt)

#Storing Data
u = np.zeros([xvector.size, tvector.size])

#Implementing Boundary and initial Conditions

#print(u[1,:]) # = 0;
# u(end,:) = 0;
#u[:,1] = (np.exp((-1)*x)).*(sin(3*x).*sin(3*x).*sin(3*x).*sin(3*x))


# %Integrating and applying the EFD method and FDM

# for n = 1:length(tvector)-1
#     for i = 2:length(xvector)-1
#         u(i,n+1) = u(i,n) + K*(delt/(delx)^2) * (u(i+1,n) - 2*u(i,n) + u(i-1,n));
#     end
# end    


# Plotting

[xx,tt, uu] = np.meshgrid(xvector, tvector, u)
fig = plt.figure()
ax = Axes3D(fig)
surf = ax.plot_trisurf(xx, tt, uu, cmap=cm.jet, linewidth=0.1)
plt.show()

# mesh(xx,tt,u);

# xlabel('X coordinate (i)')
# ylabel('time')
# zlabel('temperature')

