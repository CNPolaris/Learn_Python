#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/21 20:00
# @FileName: 0105.一次编辑.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。
给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
'''


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        # 没做改变 0次
        if first is second:
            return True
        l_f = len(first)
        l_s = len(second)
        # 做了两次插入或删除的
        if abs(l_f - l_s) > 1:
            return False
        # 一般情况
        if l_f>l_s:
            first, second = second, first
            l=len(first)
        else:
            l=len(first)
        for i in range(0,l):
            if first[i] != second[i]:
                l = i  # 找到第一个不相同的位置
                break
        return first[l:] == second[l+1:] or first[l+1:]==second[l+1:]

test = Solution()
#first = "pale"
#second = "ple"
#first = "pales"
#second = "pal"
first = "a"
second ="b"
print(test.oneEditAway(first, second))
