#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/20 18:48
# @FileName: 223.矩形面积.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''

在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。

Rectangle Area
'''
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if A>E:
            return self.computeArea(E, F, G, H, A, B, C, D)
        l_a = abs(A - C)
        h_a = abs(B - D)
        s_a=l_a*h_a
        l_b = abs(G - E)
        h_b = abs(H - F)
        s_b=l_b*h_b
        #不重叠
        if B >= H or D <= F or C <= E:
            return s_a+s_b
        #重叠
        h_ab = abs(min(C,G)-max(A,E))
        l_ab = abs(max(B,F)-min(D,H))
        s_ab = l_ab * h_ab
        return s_b+s_a-s_ab
if __name__== '__main__':
    test=Solution()\
    #-2,-2,2,2,-2,-2,2,2
    print(test.computeArea(-3, 0, 3, 4, 0, -1, 9, 2 ))
