#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/27 14:36
# @FileName: 斐波那契求和.py
# @Author  : CNTian
# @Github  : https://github.com/CNPolaris
# @Email   ：1875091912@qq.com

def Fibonacci(n):
    if n in (1, 2):
        return 1
    while n > 2:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def divded(*x):
    s=1
    for item in x:
        s *= item
    return s


if __name__ == '__main__':
    n = input()
    x = input()
    if type(eval(n)) == str:
        print("输入有误")
        n = input()
    else:
        f = Fibonacci(eval(n))
        print(f*divded(x))
