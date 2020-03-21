#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/21 11:23
# @FileName: 15.丑数.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''


# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 6: return index
        uglynum = 1
        two = 0
        three = 0
        five = 0
        res = []
        res.append(uglynum)
        while len(res) < index:
            uglynum = min(res[two] * 2, res[three] * 3, res[five] * 5)
            res.append(uglynum)
            if uglynum % 2 == 0:
                two += 1
            if uglynum % 3 == 0:
                three += 1
            if uglynum % 5 == 0:
                five += 1
        return res[index-1]

if __name__ == '__main__':
    test = Solution()
    n = 10
    print(test.GetUglyNumber_Solution(n))
