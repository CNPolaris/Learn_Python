# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 15:08
# @FileName: 9.1.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

from numpy import *
'''
创建一个shape为(5,6)的二维全为0的ndarray对象，然后让第2,3行的第2-4列元素等于1
'''

'''
res=[[]for i in range(5)]
for i in range(5):
    for j in range(6):
        res[i].append(0)
  x=array(res)
print(x)
      
'''
x=zeros((5,6),dtype=int32)
print(x.shape)
x[1,1:4]=1
x[2,1:4]=1
print(x)
