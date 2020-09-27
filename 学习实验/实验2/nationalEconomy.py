# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 8:48
# @FileName: nationalEconomy.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris


import pandas as pd
import numpy as np
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt


class NaEcon():
    def __init__(self):
        self.data = np.load('国民经济核算季度数据.npz', allow_pickle=True)
        self.columns = self.data["columns"]
        self.values = self.data['values']
        self.dataset = pd.read_csv('nationalEconomy.csv')
        plt.rcParams['font.sans-serif'] = ['SimHei']

    # 转存csv文件，数据更加直观
    def createCSV(self):
        file = open('nationalEconomy.csv', 'a+', encoding='utf-8')
        csv_writer = csv.writer(file)
        # csv_writer.writerow(self.columns)
        for value in self.values:
            csv_writer.writerow(value)

    # 数据分析
    def analysis1(self):
        # 2000-2017年度生产总值散点图
        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111)
        self.dataset.plot(x='时间', y='国内生产总值_当季值(亿元)', kind="scatter", grid=True, fontsize=12, ax=ax,
                          alpha=0.4)
        ax.set_xlabel("年份")
        ax.set_ylabel('生产总值(亿元)')
        ax.set_title('国内生产总值_当季值(亿元)')
        plt.xticks(range(0, 70, 4), self.values[range(0, 70, 4), 1], rotation=45)
        plt.savefig('国内生产总值_当季值(亿元)散点图.png')
        plt.show()

    def analysis2(self):
        plt.figure(figsize=(8, 7))
        # 绘制散点 1
        plt.scatter(self.values[:, 0], self.values[:, 3], marker='o', c='red')
        # 绘制散点 2
        plt.scatter(self.values[:, 0], self.values[:, 4], marker='D', c='blue')
        # 绘制散点 3
        plt.scatter(self.values[:, 0], self.values[:, 5], marker='v', c='yellow')
        plt.xlabel('年份')
        plt.ylabel('生产总值（亿元）')
        plt.xticks(range(0, 70, 4), self.values[range(0, 70, 4), 1], rotation=45)
        plt.title('2000-2017 年各产业季度生产总值散点图')
        plt.legend(['第一产业', '第二产业', '第三产业'])
        plt.savefig('2000-2017 年各产业季度生产总值散点图.png')
        plt.show()

    def analysis3(self):
        plt.figure(figsize=(8, 7))  # 设置画布
        # 绘制折线图
        plt.plot(self.values[:, 0], self.values[:, 2], color='r', linestyle='--')
        plt.xlabel('年份')  # 添加横轴标签
        plt.ylabel('生产总值（亿元）')  # 添加 y 轴名称
        plt.xticks(range(0, 70, 4), self.values[range(0, 70, 4), 1], rotation=45)
        plt.title('2000-2017 年季度生产总值折线图')  # 添加图表标题
        plt.savefig('2000-2017 年季度生产总值折线图.png')
        plt.show()

    def analysis4(self):
        data = self.dataset.iloc[:, 6:]
        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111)
        xlabel = ['农林牧渔业增加值_当季值(亿元)', '工业增加值_当季值(亿元)', '建筑业增加值_当季值(亿元)', '批发和零售业增加值_当季值(亿元)', '交通运输、仓储和邮政业增加值_当季值(亿元)',
                  '住宿和餐饮业增加值_当季值(亿元)', '金融业增加值_当季值(亿元)', '房地产业增加值_当季值(亿元)', '其他行业增加值_当季值(亿元)']
        colors = ['#0000FF', '#666699', '#00FF00', '#993366', '#FF6600', '#339966', '#FF8080', '#0066CC',
                  '#993366']
        ax.set_title('2000-2017全国各行业生产值增长')
        for label, color in zip(xlabel, colors):
            self.dataset.plot(x='时间', y=label, kind='scatter', fontsize=12, ax=ax,
                              color=color)
        plt.xticks(range(0, 70, 4), self.values[range(0, 70, 4), 1], rotation=45)
        plt.savefig('2000-2017全国各行业生产值增长.png')
        plt.legend(['农业', '工业', '建筑', '批发', '交通', '餐饮', '金融', '房地产', '其他'])
        plt.show()

        # print(self.dataset.isnull().sum())


if __name__ == '__main__':
    nation = NaEcon()
    # nation.createCSV()
    nation.analysis4()
