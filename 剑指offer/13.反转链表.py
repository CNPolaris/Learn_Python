#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:15
# @FileName: 13.反转链表.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com

#反转链表
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        last=None
        while pHead!=None:
                tmp = pHead.next
                pHead.next = last
                last = pHead
                pHead = tmp
        return last