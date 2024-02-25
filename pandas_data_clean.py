import numpy as np
import pandas as pd
from numpy import nan as NA

# data = pd.Series([1, NA, 3.5, NA, 7])
# print(data)
# print(data.dropna())    #清洗缺失值（Series与Dataframe）
# print(data[data.notnull()])    #与上述清洗缺失值等价

# data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef',
#                               'Bacon', 'pastrami', 'honey ham', 'nova lox'],
#                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
# print(data)
# meat_to_animal = {
#     'bacon': 'pig',
#     'pulled pork': 'pig',
#     'pastrami': 'cow',
#     'corned beef': 'cow',
#     'honey ham': 'pig',
#     'nova lox': 'salmon'
# }
# lowercased = data['food'].str.lower()    #将food键中的字符串小写
# # print(lowercased)
# data['animal'] = lowercased.map(meat_to_animal)     #Series的map接收一个函数或一个包含映射关系的字典型对象
# print(data)
# data['food'].map(lambda x: meat_to_animal[x.lower()])   #等价于上述两者命令的综合

# data = pd.Series([1., -999., 2., -999., -1000., 3.])
# print(data.replace(-999, np.nan))  #将-999替换为NA
# print(data.replace([-999, -1000], np.nan))  #替代多个值
# print(data)

# data = pd.DataFrame(np.arange(12).reshape((3, 4)),
#                     index=['Ohio', 'Colorado', 'New York'],
#                     columns=['one', 'two', 'three', 'four'])
# print(data)
# transform = lambda x: x[:4].upper()   #lambda的大写函数
# # print(data.index.map(transform))
# data.index = data.index.map(transform)   #传递命令函数
# print(data)
# print(data.rename(index=str.title, columns=str.upper))    #对列、行标题进行修改

# ages = [20, 22, 25, 27, 21, 23, 37]
# bins = [18, 25, 35, 60]
# cats = pd.cut(ages, bins)    #将ages的数据放入沙箱，以bins为参考的沙箱
# print(cats)
# print(pd.value_counts(cats))   #放入沙箱的数据分布