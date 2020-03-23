#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/23 16:51
# @FileName: 876.链表的中间结点.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        p=head
        n=0
        while p.next:
            n+=1
            p=p.next
        if n%2==0:
            for i in range(n//2):
                head=head.next
            return head
        elif n%2!=0:
            for i in range(n//2+1):
                head=head.next
            return head
        '''
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
