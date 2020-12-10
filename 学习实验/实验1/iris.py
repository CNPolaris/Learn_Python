# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 8:23
# @FileName: Part2iris.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris

from sklearn.datasets import load_iris
import numpy as np


class Iris():
    def __init__(self):
        self.data = load_iris()
        self.target = self.data.target
        self.labels = self.data.target_names
        self.feature = self.data.feature_names
        self.attributes = self.data.data

    def clean(self):
        for d in self.attributes:
            if d in self.attributes:
                self.attributes

    def analysis(self):
        # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
        for line in self.attributes:
            sepalLength = line[0]
            sepalWidth = line[1]
            petalLength = line[2]
            petalWidth = line[3]
            print("累计和：{}".format(np.sum(line)))
            print("均值：{}".format(np.mean(line)))
            print("方差{}".format(np.std(line)))
            print("标准差{}".format(np.var(line)))
            print("====================")
        sepalLengthSort = np.sort(self.attributes, axis=0)
        # print(self.attributes)
        # print(sepalLengthSort)
        print("数组总和{}".format(np.sum(self.attributes)))
        print("均值{}".format(np.mean(self.attributes)))
        print("方差{}".format(np.std(self.attributes)))
        print("标准差{}".format(np.var(self.attributes)))
        print("最大值{}".format(np.max(self.attributes)))
        print("最小值{}".format(np.min(self.attributes)))


if __name__ == '__main__':
    iris = Iris()
    # iris.clean()
    iris.analysis()
