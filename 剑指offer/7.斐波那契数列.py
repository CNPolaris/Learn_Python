#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:10
# @FileName: 7.斐波那契数列.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）
'''
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        res=[0,1,1,2]
        while len(res)<=n:
            res.append(res[-1]+res[-2])
        return res[n]