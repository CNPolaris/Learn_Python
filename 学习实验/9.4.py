# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 15:51
# @FileName: 9.4.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
'''
创建一个长度为10的一维随机数组并排序
'''
from numpy import *
x=random.randint(1,100,10)
print(x)
print(sort(x))