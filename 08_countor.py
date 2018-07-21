import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    # the height function
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)


n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

# use plt.contourf to filling contours
# X,Y and value for (X,Y) point
plt.contourf(X,Y,f(X,Y),15,alpha=0.6,cmap=plt.cm.cool)

# use plt.contour to add contour lines
C = plt.contour(X,Y,f(X,Y),15,colors='white')

# adding label
plt.clabel(C,inline=True,fontsize=8)



plt.xticks(())
plt.yticks(())


plt.show()
