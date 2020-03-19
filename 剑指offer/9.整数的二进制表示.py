#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:12
# @FileName: 9.整数的二进制表示.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n>=0:
            t=bin(n)[2:]  #bin()方法可以用来获取整数的二进制表示
            c=t.count('1')  #count()方法可以用来统计str中某一字符出现的次数
        else:
            t=bin((1<<32)-1&n)  #负数使用补码表示，bin((1<<32)-1)&n)可以获得32位的n的补码
            c=t.count('1')
        return c