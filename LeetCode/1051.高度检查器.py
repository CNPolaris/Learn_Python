#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/20 18:16
# @FileName: 1051.高度检查器.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。
请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。
注意，当一组学生被选中时，他们之间可以以任何可能的方式重新排序，而未被选中的学生应该保持不动。
'''
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res=heights
        #print(res)
        heights=sorted(heights)
        #print(heights)
        #print(res==heights)
        s=0
        for i in range(len(heights)):
            #print(s)
            if heights[i]!=res[i]:
                s= s + 1
        return s
if __name__ == '__main__':
    test=Solution()
    heights = [1,1,4,2,1,3]
    print(test.heightChecker(heights))