# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 8:41
# @FileName: tmor.py
# @Author  : CNPolaris
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import numpy as np
import time  # 导入时间库用来计算用时

"""
载入数据
"""
file_path = 'result.csv'
data = pd.read_csv(file_path)
columns = ['肝气郁结证型系数', '热毒蕴结证型系数', '冲任失调证型系数', '气血两虚证型系数',
           '脾胃虚弱证型系数', '肝肾阴虚证型系数', 'TNM分期']
data = data[columns]
print(data.head())
"""
规范化数据
"""
start = time.clock()  # 计时开始
print(u'\n转换原始数据至0-1矩阵...')
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 转换0-1矩阵的过渡函数
b = map(ct, data.to_numpy())  # 用map方式执行
data = pd.DataFrame(b).fillna(0)  # 实现矩阵转换，空值用0填充
end = time.clock()  # 计时结束
print(u'\n转换完毕，用时：%0.2f秒' % (end - start))
del b  # 删除中间变量b，节省内存
print(data)
# transaction = TransactionEncoder()
# transaction_arr = transaction.fit(data).transform(data)
#
"""
输出频繁项集
"""
frequent_itemsets = apriori(data, min_support=0.01, use_colnames=True)
# 增加字段
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
# 筛选 只看有关联的
frequent_itemsets = frequent_itemsets[frequent_itemsets['length'] > 2]
print(frequent_itemsets)  # 支持度越高说明出现的频率越高
for l, x in zip(frequent_itemsets['itemsets'], frequent_itemsets):
    print(l)
"""
输出关联规则
"""
association_rule = association_rules(frequent_itemsets, metric='confidence', support_only=True, min_threshold=0.1)
association_rule.sort_values(by='leverage', ascending=False, inplace=True)  # 关联规则可以按leverage排序
# print(association_rule['confidence'])
