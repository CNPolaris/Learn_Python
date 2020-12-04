# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 9:44
# @FileName: discretization.py
# @Author  : CNPolaris

import pandas as pd

# from sklearn.cluster import
"""
load data
"""
file_path = 'data.csv'
data = pd.read_csv(file_path)
columns = data.columns[:6]
# print(columns)
typelabel = {u'肝气郁结证型系数': 'A', u'热毒蕴结证型系数': 'B', u'冲任失调证型系数': 'C', u'气血两虚证型系数': 'D', u'脾胃虚弱证型系数': 'E', u'肝肾阴虚证型系数': 'F'}
"""
等频
"""
k = 4
keys = list(typelabel.keys())
result = pd.DataFrame()
for i in range(len(keys)):
    group = pd.qcut(data[keys[i]], k, duplicates='drop')
    # print(d3.value_counts())
    group = pd.Series(group)
    res = group.value_counts()
    dic = {}
    for g in range(0, 4):
        # print(res.index[g])
        dic[str(res.index[g])] = typelabel[keys[i]] + str(g + 1)
    # print(dic)
    # print("\n")
    for n in group:
        for d in dic.items():
            if d[0] == str(n):
                group.replace(n, d[1], inplace=True)
            # print(d)
    result.insert(i, keys[i], group)
    # result[keys[i]] = group
    # print(group)
print("\n\n")
labels = ["病程阶段", "TNM分期", "转移部位", "确诊后几年发现转移"]
for label, i in zip(labels, range(6, 10)):
    result.insert(i, label, data[label])
result.reset_index()
print(result)
result.to_csv('result.csv')
