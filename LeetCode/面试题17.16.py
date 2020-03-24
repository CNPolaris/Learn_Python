#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/24 17:16
# @FileName: 面试题17.16.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com

'''
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
'''
class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)#只计算一次可以省时间
        if l==0:return 0
        if l==1:return nums[0]
        '''
        t=nums[0]
        sum=max(nums[0:2])
        for i in range(2,len(nums)):
            next=max(sum,t+nums[i])
            t=sum
            sum=next
        return sum
        '''
        now,last=0,0
        for i in range(l):
            temp=last
            last=now
            now=max(temp+nums[i],now)
           #last,now=now,max(last+nums[i],now)
        return now
num=[1,2,3,1]
#num=[2,7,9,3,1]
#num=[2,1,4,5,3,1,1,3]
test=Solution()
print(test.massage(num))