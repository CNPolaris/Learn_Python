# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 9:06
# @FileName: apriori.py
# @Author  : CNPolaris

from apriori_python import apriori
import numpy as np
import pandas as pd

"""
数据初始化
"""
file_path = 'menu_orders.csv'
outputfile = 'apriori_rules.csv'
data = pd.read_csv(file_path)


def connect_string(x, ms):
    x = list(map(lambda i: sorted(i.split(ms)), x))
    l = len(x[0])
    r = []
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i][:l - 1] == x[j][:l - 1] and x[i][l - 1] != x[j][l - 1]:
                r.append(x[i][:l - 1] + sorted([x[j][l - 1], x[i][l - 1]]))
    return r


def find_rule(d, support, confidence, ms=u'--'):
    result = pd.DataFrame(index=['support', 'confidence'])  # 定义输出结果

    support_series = 1.0 * d.sum() / len(d)  # 支持度序列
    column = list(support_series[support_series > support].index)  # 初步根据支持度筛选
    k = 0
    while len(column) > 1:
        k = k + 1
        print(u'\n 正在进行第%s 次搜索...' % k)
        column = connect_string(column, ms)
        print(u'数目：%s...' % len(column))
        sf = lambda i: d[i].prod(axis=1, numeric_only=True)  # 新一批支持度的计算函数

        # 创建连接数据，这一步耗时、耗内存最严重。当数据集较大时，可以考虑并行运算优化。
        d_2 = pd.DataFrame(list(map(sf, column)), index=[ms.join(i) for i in column]).T

        support_series_2 = 1.0 * d_2[[ms.join(i) for i in column]].sum() / len(d)  # 计算连接后的支持度
        column = list(support_series_2[support_series_2 > support].index)  # 新一轮支持度筛选
        support_series = support_series.append(support_series_2)
        column2 = []

        for i in column:  # 遍历可能的推理，如{A,B,C}究竟是 A+B-->C 还是 B+C-->A 还是C+A-->B？
            i = i.split(ms)
            for j in range(len(i)):
                column2.append(i[:j] + i[j + 1:] + i[j:j + 1])

        cofidence_series = pd.Series(index=[ms.join(i) for i in column2])  # 定义置信度序列

        for i in column2:  # 计算置信度序列
            cofidence_series[ms.join(i)] = support_series[ms.join(sorted(i))] / support_series[ms.join(i[:len(i) - 1])]

        for i in cofidence_series[cofidence_series > confidence].index:  # 置信度筛选
            result[i] = 0.0
            result[i]['confidence'] = cofidence_series[i]
            result[i]['support'] = support_series[ms.join(sorted(i.split(ms)))]

    result = result.T.sort_values(['confidence', 'support'], ascending=False)  # 结果整理，输出
    print(u'\n 结果为：')
    print(result)
    return result


print(u'\n 转换原始数据至 0-1 矩阵...')
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 转换 0-1 矩阵的过渡函数
b = map(ct, data.to_numpy())  # 用 map 方式执行
data = pd.DataFrame(list(b)).fillna(0)  # 实现矩阵转换，空值用 0 填充
print(u'\n 转换完毕。')
del b  # 删除中间变量 b，节省内存
support = 0.2  # 最小支持度
confidence = 0.5  # 最小置信度
ms = '---'  # 连接符，默认'--'，用来区分不同元素，如 A--B。需要保证原始表格中不含有该字符
find_rule(data, support, confidence, ms).to_csv(outputfile)  # 保存结果
