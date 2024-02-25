import pandas as pd
import sys
import numpy as np
import requests

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)

# df = pd.read_csv('examples.csv')     #载入csv文件
# print(df)
#
# df2 = pd.read_csv('examples2.csv')
# print(df2)
# names = ['a', 'b', 'c', 'd', 'message']
# df3 = pd.read_csv('examples2.csv', names=names, index_col='message')
# print(df3)

# data = pd.read_csv('ex3.csv')     #输出CSV文件（）以逗号隔开
# print(data)
# data.to_csv('out.csv')
# data.to_csv(sys.stdout, sep='|')   #sys.sdtout命令让输出的文件在命令台显示
# data.to_csv(sys.stdout, na_rep='NULL')
# data.to_csv(sys.stdout, index=False, header=False)

# datas = pd.date_range('1/1/2000', periods=7)   #生成一个数据日期
# print(datas)
# ts = pd.Series(np.arange(7), index=datas)
# print(ts)
# ts.to_csv('out_date', header=False)   #to_csv() 方法默认会将 DataFrame 或 Series 对象的列名写入到 CSV 文件的第一行

# data = pd.read_json('example.json')    #处理json数据
# print(data)

#利用pandas库打开excel文件的方法
# xlsx = pd.ExcelFile('/Users/neo/云桌面报价清单0201-X86.xlsx')    #先通过路径传入
# example = pd.read_excel(xlsx)  #利用pandas读取文件
# writer = pd.ExcelWriter('example_excel.xlsx')   #创建一个Excel读写实例，空白excel文件
# example.to_excel(writer)  #将数据存入读写到实例中
# writer.close()  #保存实例



# url = 'https://api.github.com/repos/pandas-dev/pandas/issues'    #与web api的交互
# resp = requests.get(url)
# # print(resp)
# data = resp.json()     #数据转换为列表
# # print(type(data))
# issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
# print(issues)
# issues.to_csv('issues.csv')
