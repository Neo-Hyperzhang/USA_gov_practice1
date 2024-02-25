import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# data = np.arange(10)
# print(data)
# plt.plot(data)
# plt.show()

# fig = plt.figure()   #生成一个新的图片，matplotlib所绘制的图位于Figure对象中
# ax1 = fig.add_subplot(2, 2, 1)   #在图表中添加一个子图，并返回一个 Axes 对象。这个子图位于一个 2x2 的网格中的第一个位置
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# plt.plot(np.random.randn(50).cumsum(), 'k--')  #当前活动的子图（即最后一个添加的子图）中绘制一条折线图,k--' 参数指定了绘制的折线的样式
# _ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))
# fig, axes = plt.subplots(2, 3)  #又创建一个新的图片
# plt.show()


# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(np.random.randn(1000).cumsum(), 'k', label='one')  #cumsum计算随机数的累积和
# ax.plot(np.random.randn(800).cumsum(), 'k--', label='two')   #共两个图表
# ticks = ax.set_xticks([0, 250, 500, 750, 1000])     #设置x轴的值
# labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],   #设置x值的标签
#                             rotation=30, fontsize='small')
# ax.set_title('my first page about matplotlib')
# ax.set_xlabel('stages')
# ax.legend(loc='best')    #指定图例的位置
# # plt.show()
# plt.savefig('first.png', dpi=400, bbox_inches='tight')  #保存图片
# props = {
#     'title': 'first page',
#     'xlabel': 'stages'
# }
# ax.set(**props)   #批量设置绘图属性

# s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
# s.plot()    #Series对象的索引作为x轴（也可禁用）
# plt.show()

# df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),      #行索引变为x轴的值
#                   columns=['A', 'B', 'C', 'D'],
#                   index=np.arange(0, 100, 10))
# print(df)
# df.plot()
# plt.show()

# fig, axes = plt.subplots(2, 1)
# data = pd.Series(np.random.rand(16), index=list('abcedfghijklmnop'))
# data.plot.bar(ax=axes[0], color='k', alpha=0.7)   #直接画柱状图
# data.plot.barh(ax=axes[1], color='k', alpha=0.7)
# plt.show()

# df = pd.DataFrame(np.random.rand(6, 4),
#                   index=['one', 'two', 'three', 'four', 'five', 'six'],
#                   columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
# print(df)
# df.plot.bar()
# plt.show()