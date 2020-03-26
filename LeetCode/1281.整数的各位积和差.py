#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/26 9:58
# @FileName: 1281.整数的各位积和差.py
# @Author  : CNTian
# @Github  : https://github.com/CNPolaris
# @Email   ：1875091912@qq.com
'''
给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

'''
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(n)
        sum,ans=0,1
        for i in n:
            sum+=eval(i)
            ans*=eval(i)
        return ans-sum

if __name__=='__main__':
    test=Solution()
    n = 234
    print(test.subtractProductAndSum(n))
