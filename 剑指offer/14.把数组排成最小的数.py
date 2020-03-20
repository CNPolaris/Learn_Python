#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/20 20:59
# @FileName: 14.把数组排成最小的数.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com

'''
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

# -*- coding:utf-8 -*-
from functools import cmp_to_key

class Solution:
    def cmp(self,s1, s2):
        c1 = s1 + s2
        c2 = s2 + s1
        if c1 == c2:
            return 0
        elif c1 > c2:
            return 1
        else:
            return -1
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None or len(numbers) == 0:
            return ""
        res = sorted(numbers, key=cmp_to_key(lambda x, y: self.cmp(str(x) + str(y), str(y) + str(x))))
        s = ''
        for i in res:
            s += str(i)
        return s


if __name__ == '__main__':
    test = Solution()
    num = {32, 3, 321}
    print(test.PrintMinNumber(num))
