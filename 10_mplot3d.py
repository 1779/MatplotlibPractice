import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

#X,Y value
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2+Y**2)
# height vlalue
Z = np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,
                cmap=plt.get_cmap('hot'))
ax.contourf(X,Y,Z,zdir='z', offset=-2,cmap='cool')
ax.set_zlim(-2,2)



plt.show()
