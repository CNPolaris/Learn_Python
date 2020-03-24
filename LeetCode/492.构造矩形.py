#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/23 22:07
# @FileName: 492.构造矩形.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com

'''
作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。
现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。
要求：
1. 你设计的矩形页面必须等于给定的目标面积。
2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。
3. 长度 L 和宽度 W 之间的差距应当尽可能小。
'''
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        ans=[area,area/area]
        while ans[-2]>=ans[-1] and ans[-2]*ans[-1]==area:
            ans.append(ans[-2]-1)
            ans.append(area/ans[-1])
        return ans[-4:-2]
test=Solution()
s=4
print(test.constructRectangle(s))
