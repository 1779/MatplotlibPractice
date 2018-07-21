import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 50)
y1 = 2*x+1
y2 = x**2
y3 = x**3

plt.figure()
plt.plot(x,y1)

plt.figure(num=3, figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=2.0,linestyle='--')
plt.plot(x,y3,color='yellow',linewidth=3.0,linestyle='-')

plt.show()
