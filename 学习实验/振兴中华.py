#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/25 9:47
# @FileName: 振兴中华.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com

def fibonacci(x,y):
    if x==0 or y==0:
        return 1
    else:
        return fibonacci(x-1,y)+fibonacci(x,y-1)+1

print(fibonacci(3,3))
