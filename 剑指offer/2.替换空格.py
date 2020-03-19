#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:05
# @FileName: 2.替换空格.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
2.替换空格
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则
经过替换之后的字符串为We%20Are%20Happy。
'''
class Solution:
    def replaceSpace(self,s):
        t=""
        for i in iter(s):
            if i==" ":
                #str.replace(old，new)不会改变原来str
                t+="%20"
                continue
            else:
                t+=i
        return t
#测试
test=Solution()
print(test.replaceSpace("We Are Happy"))
