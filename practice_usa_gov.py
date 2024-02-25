import json
from collections import defaultdict
from collections import Counter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



path = 'example.txt'
records = [json.loads(line) for line in open(path)]  #转换为列表嵌套字典
#筛选出时区
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
# print(time_zones[0:10])



#仅使用标准库处理
def get_counts(sequence):
    counts1 = {}
    for x in sequence:
        if x in counts1:
            counts1[x] += 1
        else:
            counts1[x] = 1
    return counts1


def get_counts2(sequence):
    counts2 = defaultdict(int)  #值初始化为1
    for x in sequence:
        counts2[x] += 1
    return counts2


def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

#算时区个数——以下皆为解决方式（不同方法）
# counts = get_counts(time_zones)
# print(counts['America/New_York'])
# print(len(time_zones))
# print(top_counts(counts))

#使用collection标准库
# counts = Counter(time_zones)
# print(counts.most_common(10))

#使用pandas库
frame = pd.DataFrame(records)   #嵌套序列的每个元素通常对应 DataFrame 的一行，而内部序列的元素对应 DataFrame 的列
frame.info()   #返回Dataframe的一些基本信息
# print(frame)
# print(frame['tz'][:10])
tz_counts = frame['tz'].value_counts()
# print(tz_counts)

# clean_tz = frame['tz'].fillna('missing')  #数据可视化前，先对无效数据进行清理
# clean_tz[clean_tz == ''] = 'unknown'
# tz_counts = clean_tz.value_counts()   #对唯一量进行统计排序
# subset = tz_counts[:10]
# sns.barplot(y=subset.index, x=subset.values)  #利用seaborn库进行画图
# plt.show()  #输出matplotlib的子库pyplot进行输出画像

results = pd.Series([x.split()[0] for x in frame.a.dropna()])  #选中frame中名为a的列再对其无效值进行清除
# print(results[:5])
# print(results.value_counts()[:8])
cframe = frame[frame.a.notnull()]   #选取frame中a列中不为空的数据
# np.where(condition, x, y)：根据条件 condition，返回一个与 condition 维度相同的数组，
# 数组中的每个元素根据 condition 的值选择 x 或 y
cframe['os'] = np.where(cframe['a'].str.contains('Windows'),
                        'Windows', 'Not Windows')


# GroupBy 对象是 Pandas 中的一种数据结构，它表示根据某些标准将数据分组后的结果
# cframe.groupby(['tz', 'os'])：根据 'tz'（时区）和 'os'（操作系统）这两列的值进行分组，得到一个 GroupBy 对象 by_tz_os
# by_tz_os.size()：计算每个分组的大小，即每个时区下每个操作系统的计数
# unstack()：将多级索引（时区和操作系统）转换为二维表格形式，其中行索引为时区，列索引为操作系统，值为计数
# fillna(0)：填充缺失值为 0
by_tz_os = cframe.groupby(['tz', 'os'])
agg_counts = by_tz_os.size().unstack().fillna(0)
# print(agg_counts[:10])
# print(type(agg_counts))

# agg_counts.sum(1)：对 DataFrame agg_counts 按行求和，得到一个 Series 对象，其中每个元素表示对应行的所有列的和
# argsort()：对求和后的 Series 进行排序，返回排序后的索引数组，索引数组中的元素表示原始 Series 中的元素在排序后的位置
# 根据索引数组中的索引取出 agg_counts DataFrame 中对应的行，得到出现频率最高的 10 个时区及其对应的计数
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer[-10:])
print(count_subset)
# print(agg_counts.sum(1).nlargest(10))   #等同于上述89.90的命令

# 数据可视化
# 重新清洗数据
# stack() 方法用于将 DataFrame 的列标签（列索引）转换为行标签（行索引）
# count_subset.reset_index()：重置索引，将原来的多级索引（即时区和操作系统）转换为普通的整数索引，并将索引中的级别作为列添加到 DataFrame 中
count_subset = count_subset.stack()
print(count_subset)
count_subset.name = 'total'
count_subset = count_subset.reset_index()
print(count_subset)
# sns.barplot(x='total', y='tz', hue='os', data=count_subset)


def norm_total(group):
    group['normal_total'] = group.total/group.total.sum()
    return group


results_end = count_subset.groupby('tz').apply(norm_total)   # apply() 方法用于将指定的函数应用到分组的每个子组上
sns.barplot(x='normal_total', y='tz', hue='os', data=results_end)
plt.show()

# count_subset.total 是 count_subset DataFrame 中的一个 Series，表示每个时区的总计数值
# g.total.transform('sum') 则是对整个 DataFrame g 中的 'total' 列进行求和操作，返回一个 Series，表示每个时区的总计数值。
# g = count_subset.groupby('tz')
# results_end2 = count_subset.total/g.total.transform('sum')
# sns.barplot(x='normal_total', y='tz', hue='os', data=results_end2)
# plt.show()