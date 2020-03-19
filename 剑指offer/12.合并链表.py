#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:14
# @FileName: 12.合并链表.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
'''
# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        temp = ListNode(666)
        temphead = temp
        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                temp.next= pHead2
                pHead2 = pHead2.next
            else:
                temp.next= pHead1
                pHead1 = pHead1.next

            temp = temp.next
        if pHead1:
            temp.next = pHead1
        elif pHead2:
            temp.next = pHead2

        return temphead.next