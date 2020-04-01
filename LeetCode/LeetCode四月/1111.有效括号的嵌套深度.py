# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 15:46
# @FileName: 1111.有效括号的嵌套深度.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

'''
有效括号字符串 定义：对于每个左括号，都能找到与之对应的右括号，反之亦然。详情参见题末「有效括号字符串」部分。
嵌套深度 depth 定义：即有效括号字符串嵌套的层数，depth(A) 表示有效括号字符串 A 的嵌套深度。详情参见题末「嵌套深度」部分。
'''
import unittest
class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """

        class Solution:
            def maxDepthAfterSplit(self, seq):
                ans = []
                d = 0
                for c in seq:
                    if c == '(':
                        d += 1
                        ans.append(d % 2)
                    if c == ')':
                        ans.append(d % 2)
                        d -= 1
                return ans
class Test(unittest.TestCase):
    def Test_1(self):
        test=Solution()
        seq = "(()())"
        self.assertEqual(test.maxDepthAfterSplit(seq),[0,1,1,1,1,0])

if __name__=='__main__':
    unittest.main()
