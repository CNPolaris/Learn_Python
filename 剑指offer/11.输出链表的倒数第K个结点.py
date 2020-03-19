#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:13
# @FileName: 11.输出链表的倒数第K个结点.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com

#输出链表的倒数第k个结点
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res=[]
        while head!=None:
            res.append(head)
            head=head.next
        if k<1 or k>len(res):
            return
        return res[-k]
