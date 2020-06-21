# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 15:02
# @FileName: 人口收入普查数据探索.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris


import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 使用类进行封装
class HumanExplore():

    def __init__(self):
        # 准备数据集
        self.data = pd.read_csv('https://labfile.oss.aliyuncs.com/courses/1283/adult.data.csv')
        self.data.head()

    # 统计数据集中的男女数量
    def count_sex(self):
        sex_data = self.data['sex']
        count = sex_data.value_counts()
        print(count)

    # 数据集中男女的平均年龄各是多少
    def aver_age(self):
        age_data = self.data['age'].groupby(self.data['sex'])
        average = age_data.mean()
        print(average)

    # 年收入超过 50K 和低于 50K 人群年龄的平均值和标准差
    def explore_year_income(self):
        income_data = self.data['age'].groupby(self.data['salary'])
        income_mean = income_data.mean()
        income_std = income_data.std()
        print(income_mean)
        print(income_std)

    # 年收入超过 50K 的人群是否都接受过高中以上教育
    def about_education(self):
        eduction_data = self.data[self.data['salary'] == '>50K']['education'].unique()
        print(eduction_data)

    # 统计男性高收入人群中已婚和未婚（包含离婚和分居）人群各自所占数量。
    def about_married(self):
        marrid_data = self.data[(self.data['sex'] == 'Male') &
                                (self.data['marital-status'].isin(['Never-married',
                                                                   'Separated', 'Divorced']))]['salary'].value_counts()
        print(marrid_data)

    # 统计数据集中最长周工作小时数及对应的人数，并计算该群体中收入超过 50K 的比例
    def about_work_time(self):
        week_max=self.data['hours-per-week'].max()
        count_max=self.data[self.data['hours-per-week']==week_max].shape[0]
        proportion=self.data[(self.data['hours-per-week']==week_max)&
                             (self.data['salary']=='>50K')].shape[0]/count_max
        print(week_max)
        print(proportion)

if __name__ == '__main__':
    human = HumanExplore()
    # human.count_sex()
    # human.aver_age()
    # human.explore_year_income()
    # human.about_education()
    # human.about_married()
    human.about_work_time()
