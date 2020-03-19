#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:12
# @FileName: 10.数组的奇偶分离.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
from collections import deque
class Solution:
    def reOrderArray(self, array):
        # write code here
        t=deque()
        x=len(array)
        for i in range(x):
            if array[x-i-1]%2!=0:
                t.appendleft(array[x-i-1])
            if array[i]%2==0:
                t.append(array[i])
        return list(t)
