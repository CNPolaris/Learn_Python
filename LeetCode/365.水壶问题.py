#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/21 12:36
# @FileName: 365.水壶问题.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com

'''
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
(找最大约数)
'''
import math
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x==z or y==z or (max(x,y)-min(x,y))==z:
            return True
        if x+y<z:
            return False
        return z%math.gcd(x,y)==0

if __name__=='__main__':
    test=Solution()
    '''x = 3
    y = 5
    z = 4'''
    x = 2
    y = 6
    z = 5
    print(test.canMeasureWater(x,y,z))