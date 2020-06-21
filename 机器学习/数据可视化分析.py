# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 17:17
# @FileName: 数据可视化分析.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris


import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
warnings.filterwarnings('ignore')


class DataVisualization():
    # 构造方法
    def __init__(self):
        # 准备数据
        self.data = pd.read_csv('https://labfile.oss.aliyuncs.com/courses/1283/telecom_churn.csv')
        self.data.head()

    # 直方图和密度图的简单绘制
    # 能够首先了解到数据的特征值分布
    def draw_line_density(self):
        # 选择数据源
        features = ['Total day minutes', 'Total intl calls']
        # 最简单的查看数值变量分布的方法是使用DataFrame的hist方法绘制直方图
        self.data[features].hist(figsize=(12, 7))

        # 密度图的绘制，是理解数值变量分布的另一个方法，相对直方图更加清晰
        self.data[features].plot(kind='density', subplots=True, layout=(1, 2),
                                 sharex=False, figsize=(12, 7), legend=False, title=features)
        # 绘制图形的话也可以先创建画布，然后在不同的画布上绘制可视化图形
        plt.show()

    # 箱型图的绘制
    """
    5个参数： 
    下边缘（Q1），表示最小值； 
    下四分位数（Q2），又称“第一四分位数”，等于该样本中所有数值由小到大排列后第25%的数字； 
    中位数（Q3），又称“第二四分位数”等于该样本中所有数值由小到大排列后第50%的数字； 
    上四分位数（Q4），又称“第三四分位数”等于该样本中所有数值由小到大排列后第75%的数字； 
    上边缘（Q5），表述最大值。
    """

    def draw_box_plot(self):
        sns.boxplot(y='Total intl calls', data=self.data)
        plt.show()

    # 绘制小提琴图
    """
    小提琴图 (Violin Plot)是用来展示多组数据的分布状态以及概率密度。
    这种图表结合了箱形图和密度图的特征，主要用来显示数据的分布形状。
    跟箱形图类似，但是在密度层面展示更好。在数据量非常大不方便一个一个展示的时候小提琴图特别适用。
    """

    def draw_violin_plot(self):
        # 准备画布
        fig = plt.figure(figsize=(12, 7))
        ax1 = fig.add_subplot(121)
        ax1.set_title("violin_plot")
        ax2 = fig.add_subplot(122)
        ax2.set_title("violin_plot")
        # 载入数据
        data1 = self.data['Total intl calls']
        ax1.violinplot(data1, showmeans=False, showmedians=True)

        data2 = self.data['Total day minutes']
        ax2.violinplot(data2, showmeans=False, showmedians=True)

        plt.show()

    # 数据描述
    """
    除图形工具外，还可以使用 DataFrame 的  describe() 方法来获取分布的精确数值统计。
    """

    def data_descrtbe(self):
        print(self.data.describe())

    # 条形图
    def draw_count_plot(self):
        # 频率表的图形化表示就是条形图,创建条形图的最简单的办法是通过seaborn的countplot方法进行生成
        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111)
        ax.set_title("count_plot", fontsize=18)
        # 获得频率表的方法
        # self.data['Churn'].values_counts()
        sns.countplot(x='Customer service calls', data=self.data, ax=ax)
        plt.show()

    # 相关矩阵
    """
    相关矩阵可揭示数据集中的数值变量的相关性。这一信息很重要，因为有一些机器学习算法（比如，线性回归和逻辑回归）不能很好地处理高度相关的输入变量。
    """
    def draw_heatmap(self):
        # 先去除数据集中非数值的数据项
        data=list(set(self.data.columns)-set(['State', 'International plan', 'Voice mail plan',
                      'Area code', 'Churn', 'Customer service calls']))
        # 通过corr方法计算没对特征间的相关性
        corr_matrix=self.data[data].corr()
        # 根据所得到的相关矩阵绘制出一个基于色彩编码的矩阵
        sns.heatmap(corr_matrix,cmap='RdYlGn',center=0)
        plt.show()
if __name__ == '__main__':
    visualization = DataVisualization()
    # visualization.draw_line_density()
    # visualization.draw_box_plot()
    # visualization.draw_violin_plot()
    # visualization.data_descrtbe()
    # visualization.draw_count_plot()
    visualization.draw_heatmap()