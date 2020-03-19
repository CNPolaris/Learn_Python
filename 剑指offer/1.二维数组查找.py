#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:03
# @FileName: 1.二维数组查找.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
1.二维数组的查找
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
'''
#二位数组的查找
#我的解法
class solution:
    def Find(self,target,array):
        rows=len(array)
        cols=len(array[0])
        n=rows*cols
        k=0
        t=list(range(n))
        for i in range(rows):
            for j in range(cols):
                t[k]=array[i][j]
                k+=1
        if target in t:
            return True
        else:
            return False
        print(t)
        return True
#测试
target = 15
array = [[1,2,3],[4,5,6],[7,8,9],[10,12,13]]
answer = solution()
print(answer.Find(target,array))
'''
#第二种解法
def Find(self, target, array):
    # write code here
    rows = len(array)
    cols = len(array[0])
    if rows > 0 and cols > 0:
        #找到最右上角元素
        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            #如果右上角刚好是的就直接返回
            if target == array[row][col]:
                return True
            #如果比右上角小，就往前移一列
            elif target < array[row][col]:
                col -= 1
            #如果比右上角大，就往下移一行
            else:
                row += 1
    return False
'''
