# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 8:21
# @FileName: boston.py
# @Author  : CNPolaris

from sklearn.datasets import load_boston
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import seaborn as sns

"""
载入数据集
"""
bostonData = load_boston()
target = bostonData.target  # 回归值 Y
features = bostonData.feature_names  # 特征
attributes = bostonData.data  # 特征值 X
data = pd.DataFrame(attributes, columns=features)  # 特征值拼接
data['MEDV'] = target
mpl.rcParams['axes.unicode_minus'] = False

"""
特征选取
"""


# 手工选取
def dataLook():
    fig = plt.figure(figsize=(12, 7))
    colors = ['#0000FF', '#666699', '#00FF00', '#993366', '#FF6600', '#339966', '#FF8080', '#0066CC', '#993366',
              '#FFCC99', '#99CC00']
    for label, color in zip(features, colors):
        plt.scatter(data[label], data['MEDV'], marker='o', color=color)
    plt.xlabel = "target"
    plt.legend(features)
    plt.show()


# 相关系数矩阵分析选取
def correlation():
    print('pearson\n', data.corr(method='pearson'))  # 皮尔逊相关系数
    print('kendall\n', data.corr(method='kendall'))  # 肯德尔秩相关系数
    print('spearman\n', data.corr(method='spearman'))  # 斯皮尔曼秩相关系数
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(111)
    corr = data[features].corr(method='pearson')
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, cmap='RdYlGn', center=0, annot=True)
    plt.yticks(fontsize=12)
    plt.xticks(fontsize=12)
    plt.title('相关系数矩阵')
    plt.show()


# PCA
def pca():
    n_components = 12
    X = StandardScaler().fit_transform(attributes)
    pca = PCA(n_components=n_components)
    pca.fit(X)
    plt.plot(pca.explained_variance_)
    plt.xlabel('component')
    plt.ylabel('explained variance')
    print(pca.singular_values_)
    # print(components)
    print("前{}个主成分解释了数据中{:.2f}%的变化".format(n_components, sum(pca.explained_variance_ratio_) * 100))


"""
训练预测
"""
train_X, test_X, train_Y, test_Y = train_test_split(data[features], data['MEDV'], test_size=0.2)

decision = DecisionTreeRegressor()
decision.fit(train_X, train_Y)
y_pre_decision = decision.predict(test_X)
acc_decision_tree = round(decision.score(test_X, test_Y), 6)
print('score 准确率为 %.4lf' % acc_decision_tree)
# print(y_pre_decision)

linear = LinearRegression()
linear.fit(train_X, train_Y)
y_pre_linear = linear.predict(test_X)
acc_liner = round(linear.score(test_X, test_Y), 6)
print('score 准确率为 %.4lf' % acc_liner)


knn = KNeighborsRegressor()
knn.fit(train_X, train_Y)
y_pre_knn = knn.predict(test_X)
acc_knn = round(knn.score(test_X, test_Y), 6)
print('score 准确率为 %.4lf' % acc_knn)


test_data = pd.concat([test_X, test_Y], axis=1)
plt.figure(figsize=(12, 7))
for label in features:
    plt.scatter(test_X[label], y_pre_decision, marker='o', c='#0000FF')
    plt.scatter(test_X[label], test_Y, marker='o', c='#993366')
plt.legend(['predict', 'test'])
plt.ylabel('money')
plt.show()
