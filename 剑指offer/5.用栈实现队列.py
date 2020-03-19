#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:08
# @FileName: 5.用栈实现队列.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
#题目描述
#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
        return self.stack2.pop()

'''
# java版本
import java.util.Stack;

public


class Solution {
Stack < Integer > stack1 = new Stack < Integer > ();
Stack < Integer > stack2 = new Stack < Integer > ();

public void push(int node) {
stack1.push(node);
}

public int pop() {
if (stack2.isEmpty()){


while (!stack1.isEmpty()){
stack2.push(stack1.pop());
}
}
return stack2.pop();
}
}
'''
