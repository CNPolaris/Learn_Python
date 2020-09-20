# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 10:40
# @FileName: 心血管疾病数据探索分析.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib import rcParams
import warnings

warnings.filterwarnings('ignore')

# 设置seaborn绘图全局参数
sns.set()
sns.set_context(
    "notebook",
    font_scale=1.5,
    rc={
        "figure.figsize": (11, 8),
        "axes.titlesize": 18
    }
)

rcParams['figure.figsize'] = 11, 8


class DiseaseData():
    # 构造函数
    def __init__(self):
        # 装载数据
        self.data = pd.read_csv('https://labfile.oss.aliyuncs.com/courses/1283/mlbootcamp5_train.csv', sep=';')
        self.data.head()


if __name__ == '__main__':
    disease = DiseaseData()
