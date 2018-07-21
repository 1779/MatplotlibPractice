import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,4,50)   
y = 0.5*x+1



plt.figure()
plt.plot(x,y)

plt.xlim((-2,4))
plt.ylim((-1,3))

x_ticks = np.linspace(-2,4,7)
y_ticks = np.linspace(-1,3,5)

plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.xlabel('X')
plt.ylabel('Y')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


##################################################
x0 = 1
y0 = 0.5*x0+1
plt.scatter(x0,y0,color='r') # 画出点x0,y0
plt.plot([x0,x0],[y0,0],'y--',lw=2.5) # 画出一条从x0,y0到x 轴的垂线

# method 1
#################################################
plt.annotate(r'$0.5x+1=%s$'%y0, xy=(x0,y0), xycoords='data',
              xytext=(+30,-30), textcoords='offset points',
              fontsize=16, arrowprops=dict(arrowstyle='->',
                                           connectionstyle='arc3,rad=0.2'))
# method 2
##############

plt.text(-2,2,r'$Hello\ Tom\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':12, 'color':'c'})






plt.show()
