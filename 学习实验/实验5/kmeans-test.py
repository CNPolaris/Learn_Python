# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 8:21
# @FileName: kmeans-test.py
# @Author  : CNPolaris

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 参数初始化
file_path = 'consumption_data.csv'
outputfile = 'data_type.csv'
k = 3  # 聚类的类别
iteration = 500  # 聚类的最大循环次数
data = pd.read_csv(file_path, index_col='Id')
data_zs = 1.0 * (data - data.mean()) / data.std()  # 数据标准化
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
"""
构建模型
"""
model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration, random_state=1234)  # 分类为k类，并发数为4
model.fit(data_zs)  # 开始聚类

"""
结果打印
"""
label_count = pd.Series(model.labels_).value_counts()  # 统计各个类别的数目
kmeans_center = pd.DataFrame(model.cluster_centers_)  # 找出聚类中心
label_center = pd.concat([kmeans_center, label_count], axis=1)  # 得到聚类中心对应的类别下的数目
label_center.columns = list(data.columns) + ['类别数目']  # 重命名表头
print(label_center)

"""
结果对照
"""
result = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)  # 详细输出每个样本对应的类别
result.columns = list(data.columns) + ['聚类类别']  # 重命名表头
result.to_csv(outputfile)  # 保存结果


def density_plot(data):  # 自定义作图函数
    p = data.plot(kind='kde', linewidth=2, subplots=True, sharex=False)
    [p[i].set_ylabel(u'密度') for i in range(k)]
    plt.legend()
    return plt


pic_output = 'pd'  # 概率密度图文件名前缀
for i in range(k):
    density_plot(data[result[u'聚类类别'] == i]).savefig(u'%s%s.png' % (pic_output, i))
plt.savefig('kmeans.png')
plt.show()
