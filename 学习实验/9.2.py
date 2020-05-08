# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 15:29
# @FileName: 9.2.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

'''
使用np.random库创建一个10*10的整型ndarray对象，并打印出最大最小元素
'''
import numpy as np
x=np.random.randint(1,100,(10,10))
print(x)
print("最小值{}".format(np.min(x)))
'''
对第2题中的矩阵，计算最后两列的和
'''
s=x[-1]+x[-2]
print(sum(s))