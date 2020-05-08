# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 16:04
# @FileName: 树的遍历.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

class PyTree:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
    def insertLeft(self,value):
        self.left=PyTree(value)
        return self.left
    def insertRight(self,value):
        self.right=PyTree(value)
        return self.right
    def show(self):
        print(self.data)

def preorder(node):
    if node.data:
        node.show()
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)

def Middle(node):
    if node.data:
        if node.left:
            Middle(node.left)
        node.show()
        if node.right:
            Middle(node.right)
def Postorder(node):
    if node.data:
        if node.left:
            Middle(node.left)
        if node.right:
            Middle(node.right)
        node.show()


if __name__=='__main__':
    Root=PyTree('R')
    A=Root.insertLeft('A')
    C=A.insertLeft('C')
    D=A.insertRight('D')
    F=D.insertLeft('F')
    G=D.insertRight('G')
    B=Root.insertRight('B')
    E=B.insertRight('E')
    # Root.show()
    # Root.left.show()
    # Root.right.show()
    # A=Root.left
    # A.left.show()
    # Root.left.right.show()
    print("前序")
    print(preorder(Root))
    print("中序")
    print(Middle(Root))
    print("后序")
    print(Postorder(Root))