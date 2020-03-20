#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/20 17:10
# @FileName: 61.旋转链表.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
'''


# Definition for singly-linked list.
import json


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return 0
        if not head.next: return head
        if k == 0: return head
        p = head
        l = 1
        #把单链表改成循环链表
        while head.next:
            head = head.next
            l += 1
        head.next = p
        #把头指针往后移
        for i in range(l - k % l - 1):
            p = p.next
        #此时p的后面一个节点是新的头结点
        new_head = p.next
        #把循环链表断开
        p.next = None
        #返回新的链表头
        return new_head


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def stringToInt(input):
    return int(input)


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            head = stringToListNode(line)
            line = lines.next()
            k = stringToInt(line)

            ret = Solution().rotateRight(head, k)

            out = listNodeToString(ret)
            print
            out
        except StopIteration:
            break


if __name__ == '__main__':
    main()