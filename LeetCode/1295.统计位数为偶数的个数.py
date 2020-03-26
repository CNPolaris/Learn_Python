#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/26 15:18
# @FileName: 1295.统计位数为偶数的个数.py
# @Author  : CNTian
# @Github  : https://github.com/CNPolaris
# @Email   ：1875091912@qq.com
'''
给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。
'''
import unittest


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            l = 0
            while i > 0:
                i = i // 10
                l += 1
            if l % 2 == 0:
                ans += 1
            # ans.append(l)
        return ans


class TestfindNumbers(unittest.TestCase):
    def test1(self):
        test = Solution()
        nums = [12, 345, 2, 6, 7896]
        self.assertEqual(test.findNumbers(nums), 2)

    def test2(self):
        test2 = Solution()
        nums = [555, 901, 482, 1771]
        self.assertEqual(test2.findNumbers(nums), 1)


if __name__ == '__main__':
    unittest.main()
