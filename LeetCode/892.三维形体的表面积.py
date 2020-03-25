#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/25 10:52
# @FileName: 892.三维形体的表面积.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N=len(grid)
        s1=0    #s1放每个位置的自身面积
        '''
        for i in range(N):
            for j in range(N):
                if grid[i][j]!=0:
        '''
        s2=0    #S2放之间重叠的面积数
        for i in range(N):
            for j in range(N):
                if grid[i][j]!= 0:  #当前位置不为0时
                    s1 += grid[i][j] * 4 + 2 #累加面积
                    if j<N-1: #看这个位置的右边
                        s2+=min(grid[i][j],grid[i][j+1])
                    if i<N-1: #看这个位置的下面
                        s2+=min(grid[i][j],grid[i+1][j])
        return s1-s2*2
test=Solution()
#num=[[1,2],[3,4]]
#num=[[1,0],[0,2]]
num=[[2,2,2],[2,1,2],[2,2,2]]
print(test.surfaceArea(num))