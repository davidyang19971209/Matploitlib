import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6,6,50)
y = 2*x+1
y2 = x**2


plt.figure()
l1,= plt.plot(x,y,label='up')
l2,= plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--',label='down')

plt.xlim((-8,8))
plt.ylim((-8,8))
# plt.xlabel('I am x')
# plt.ylabel('I am y')

new_ticks = np.linspace(-8,8,16)
# print(new_ticks)
# plt.xticks(new_ticks)
# plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$',r'$bad\alpha$','normal','good','really good'])


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='blue',edgecolor='red',alpha=0.2))

x0 = 1
y0 = 2*x0+1
plt.scatter(x0,y0,s=10,color='b')
plt.plot([x0,x0],[0,y0],'k--')
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',
    xytext=(+15,-15),textcoords='offset points',
    fontsize=8,arrowprops = dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

plt.text(-6,3,r'$This\ is\ the\ some\ text.\ \mu \sigma_i \alpha_t$',
    fontdict={'size':8,'color':'r'})

plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')


plt.show()