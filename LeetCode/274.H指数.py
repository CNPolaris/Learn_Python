#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/25 21:22
# @FileName: 274.H指数.py
# @Author  : CNTian
# @Github  : https://github.com/CNPolaris
# @Email   ：1875091912@qq.com

'''
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。
编写一个方法，计算出研究者的 h 指数。
h 指数的定义: “h 代表“高引用次数”（high citations），
一名科研人员的 h 指数是指他（她）的 （N 篇论文中）至多有 h 篇论文分别被引用了至少 h 次。（
其余的 N - h 篇论文每篇被引用次数不多于 h 次。）”
'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        if not citations or max(citations) == 0:
            return 0
        citations=sorted(citations,reverse=True)
        l=len(citations)
        ans=[]
        for i in range(l):
            if citations[i]>i:
                ans.append(i)
        return max(ans)+1


test=Solution()
#citations = [3,0,6,1,5]
citations=[1,2,3,3,5,9,10]
print(test.hIndex(citations))