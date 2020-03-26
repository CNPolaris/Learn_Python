#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/26 17:07
# @FileName: 面试题16.21交换和.py
# @Author  : CNTian
# @Github  : https://github.com/CNPolaris
# @Email   ：1875091912@qq.com
'''
给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。
返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。
若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。
'''
import unittest


class Solution(object):
    def findSwapValues(self, array1, array2):
        """
        :type array1: List[int]
        :type array2: List[int]
        :rtype: List[int]
        """
        diff = sum(array1) - sum(array2)
        if diff % 2 != 0:
            return []
        diff //= 2
        for i in array1:
            if i - diff in array2:
                return [i, i - diff]
        return []


class TestfindSwapValues(unittest.TestCase):
    def test_t1(self):
        test1 = Solution()
        array1, array2 = [4, 1, 2, 1, 1, 2], [3, 6, 3, 3]  # [1, 3]
        self.assertEqual(test1.findSwapValues(array1, array2), [4, 6])

    def test_t2(self):
        test = Solution()
        array1, array2 = [1, 2, 3], [4, 5, 6]  # []
        self.assertEqual(test.findSwapValues(array1, array2), [])


if __name__ == '__main__':
    unittest.main()
