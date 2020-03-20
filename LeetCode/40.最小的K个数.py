#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/20 16:47
# @FileName: 40.最小的K个数.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
'''
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        return(arr[:k])
test=Solution()
arr = [3,2,1]
k = 2
print(test.getLeastNumbers(arr,k))

