#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:06
# @FileName: 3.从尾到头打印链表.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next

        return (res[::-1])
