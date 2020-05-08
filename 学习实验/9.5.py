# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 15:53
# @FileName: 9.5.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

'''
创建一个一维长度为15的随机矩阵和一个32随机矩阵，将前者使用reshape改为5*3的矩阵，与3*2的矩阵，求矩阵积
'''
from numpy import *

x = random.randint(1, 100, 15)
y = random.randint(1, 100, 32)
x.resize((5, 3))
y.resize((3, 2))
print(x)
print(y)
print(dot(x,y))
