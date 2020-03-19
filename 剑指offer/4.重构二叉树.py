#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:06
# @FileName: 4.重构二叉树.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
#题目描述
#输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
#- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        lon=len(pre)
        if lon==0:
            return None
        elif lon==1:
            return TreeNode(pre[0])
        else:
            root=TreeNode(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0]) + 1], tin[:tin.index(pre[0])])
            root.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
            return root