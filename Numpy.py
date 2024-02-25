import numpy as np
import matplotlib_practice.pyplot as plt
from numpy.linalg import inv, qr   #矩阵操作的标准函数集
# arr = np.array([3.7, 3.2, 0.9])
# arr1 = arr.astype(np.int32)   #产生了一个新的数组，与arr无关
# print(arr1)
# print(arr1.dtype)


# arr = np.array([[1, 2, 3], [4, 5, 6]])    #逐元素操作，无须循环
# print(arr)
# print(arr*arr)
# print(arr-arr)
# print(1/arr)
# print(arr**0.5)

# arr = np.arange(10)    #操作与列表相似
# print(arr)
# print(arr[5])
# print(arr[5:8])
# arr[5:8] = 12
# print(arr)

# arr =np.arange(10)      #数组的切片仍是原数组的一部分，并为创建新的数组
# arr_slice = arr[5:8]
# print(arr)
# print(arr_slice)
# arr_slice[1] = 12345
# print(arr)
# print(type(arr_slice))

# arr = np.empty((8, 4))    #直接用整数数组进行索引
# for i in range(8):
#     arr[i] = i
# print(arr)
# print()
# print(arr[[2, 1]])
# print(f"{arr[[-3, -5]]}\n")

# arr = np.arange(32).reshape((8, 4))     #神奇索引
# print(arr)
# print()
# print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])      #[[行，列]]
# print()
# print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])    #多次索引

# arr = np.arange(15).reshape((3,5))  #转置
# print(arr)
# print(arr.T)
# print(arr)

# arr = np.random.randn(6, 3)  #求内积
# print(f'{arr}\n')
# print(np.dot(arr.T, arr))

# arr = np.arange(10)     #一元通用函数/二元通用函数
# print(arr)
# print(type(arr))
# print(np.exp(arr))
#
# x = np.random.randn(8)
# y = np.random.randn(8)
# print(np.maximum(x, y))


# points = np.arange(-5, 5, 0.001)    #直接进行数组计算
# x, y = np.meshgrid(points, points)
# print(y)
# print()
# z = np.sqrt(x**2 + y**2)
# print(z)
# plt.imshow(z, cmap=plt.cm.gray)
# plt.colorbar()
# plt.title("Images")

# xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])   #数组的三元if的向量化版本
# yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
# cond = np.array([1, 0, 1, 1, 0])
# result = np.where(cond, xarr, yarr)    # xrr if cond else yarr
# print(result)
#
# arr = np.random.randn(4, 4)
# result = np.where(arr > 0, 2, -2)
# print(result)
# result = np.where(arr > 0, 2, arr)
# print(result)

# arr = np.random.randn(5, 4)   #基础数组统计方法
# print(arr)
# print(arr.mean())
# print(np.mean(arr))
# print(arr.sum())

# # arr = np.random.randn(6)     #对数组进行排序
# # print(arr)
# # arr.sort()
# # print(arr)
# arr = np.random.randn(5, 3)    #0代表以列为轴，1代表以行为轴
# print(arr)
# print()
# arr.sort(1)
# print(arr)
# print()
# arr.sort(0)
# print(arr)

# arr = np.arange(10)     #对数组以文件的形式进行保存和载入
# np.save('array', arr)
# result = np.load('array.npy')
# print(result)

# x = np.array([[1, 2, 3],[4, 5, 6]])       #矩阵乘法
# y = np.array([[6, 23],[-1, 7], [8, 9]])
# print(x)
# print(y)
# # print(x.dot(y))
# # print(np.dot(x, y))
# print(np.ones(3))

# samples = np.random.normal(size=(4, 4))  #伪随机数生成，相比于python自带的random，更快的生成伪随机数组
# print(samples)

# nsteps = 1000
# draws = np.random.randint(0, 2, size=nsteps)
# steps = np.where(draws > 0, 1, -1)
# walk = steps.cumsum()
# print(walk.min())
# print(walk.max())

# arr = np.random.randn(4, 4)
# print(arr)
# walks = arr.cumsum(1)      #以行为轴进行i元素之前的累加
# print()
# print(walks)