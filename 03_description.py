import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 50)
y1 = 2*x+1
y2 = x**2

plt.figure()

plt.xlim((-2,2))
plt.ylim((-1,3))

plt.xlabel('X')
plt.ylabel('Y')

new_ticks = np.linspace(-2,2,5)
print(new_ticks) # 用于标注坐标

plt.xticks(new_ticks)
plt.yticks([-0.5,0,1.5,2])


##################################################

l1, = plt.plot(x,y2,label='up') # label用于对线起名
l2, = plt.plot(x,y1,color='red',linewidth=2.0,linestyle='--',label='down')

# plt.plot() 是有返回值的 l1由于接收返回值
# 将返回值放入handles中 必须加逗号

plt.legend(handles=[l1,l2],labels=['A','B'], loc='upper right') # 添加对线的描述，参数有handles=
                # labels= loc='best'/'upper right'/...
# 如果只想打印A 则['A',]就行









plt.show()
