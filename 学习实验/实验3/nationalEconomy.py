# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 8:23
# @FileName: nationalEconomy.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# 将数据整理成CSV文件
def make_csv():
    columns = ['year', 't', 'y']
    data = [[2007, 1, 2.9], [2008, 2, 3.3], [2009, 3, 3.6], [2010, 4, 4.4], [2011, 5, 4.8], [2012, 6, 5.2],
            [2013, 7, 5.9]]
    make = pd.DataFrame(columns=columns, data=data)
    make.to_csv('data.csv', encoding='utf-8')
    # print(data)


# make_csv()


# 载入数据
dataCSV = pd.read_csv('data.csv', encoding='utf-8')
# print(dataCSV)

t = dataCSV['t']
y = dataCSV['y']

# 散点图
plt.scatter(t, y)
# plt.show()  # 线性拟合比较好
# print(t, y)
# print(dataCSV.shape)

# 准备数据
x = dataCSV[['t']]
# print(x.head())
y = dataCSV[['y']]
# 创建模型
model = LinearRegression()
model.fit(x, y)

# 画图
plt.plot(x, y, 'g')
plt.plot(x, model.predict(x), 'r')

# plt.show()

# 预测
print(model.predict([[8]]), [0], [0])
