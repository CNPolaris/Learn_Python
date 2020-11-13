# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 11:42
# @FileName: usingMlxtend.py
# @Author  : CNPolaris

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

"""
导入数据
"""
file_path = 'menu_orders.csv'
outputfile = 'apriori_rules.csv'
data = pd.read_csv(file_path)
"""
补充数据
"""
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 转换 0-1 矩阵的过渡函数
b = map(ct, data.to_numpy())  # 用 map 方式执行
data = pd.DataFrame(b).fillna(0)  # 空值用 0 填充
"""
规范化数据
"""
transaction = TransactionEncoder()
transaction_arr = transaction.fit(data).transform(data)
# print(data)
"""
输出频繁项集
"""
frequent_itemsets = apriori(data, min_support=0.2, use_colnames=True)
# 增加字段
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
# 筛选 只看有关联的
frequent_itemsets = frequent_itemsets[frequent_itemsets['length'] > 1]
print(frequent_itemsets)  # 支持度越高说明出现的频率越高
"""
输出关联规则
"""
association_rule = association_rules(frequent_itemsets, metric='confidence', support_only=True, min_threshold=0.1)
association_rule.sort_values(by='leverage', ascending=False, inplace=True)  # 关联规则可以按leverage排序
print(association_rule)
