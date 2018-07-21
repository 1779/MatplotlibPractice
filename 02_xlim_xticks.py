import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 50)
y1 = 2*x+1
y2 = x**2
y3 = x**3

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=2.0,linestyle='--')
plt.plot(x,y3,color='yellow',linewidth=3.0,linestyle='-')

plt.xlim((-2,2))
plt.ylim((-1,3))

plt.xlabel('X')
plt.ylabel('Y')

new_ticks = np.linspace(-2,2,5)
print(new_ticks)

plt.xticks(new_ticks)
plt.yticks([-0.5,0,1.5,2],[r'$really\ bad$',r'$good\ \alpha$',r'$pretty\ good$',r'$increadable$'])


##################################################

# gca = 'get current axis'

ax = plt.gca()
ax.spines['right'].set_color('none') # 右边框不显示
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom') # X轴设置为底边
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',-1)) # -1表示坐标轴绑定在y轴-1
ax.spines['left'].set_position(('data',0))















plt.show()
