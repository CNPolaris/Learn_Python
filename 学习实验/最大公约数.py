#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/27 14:27
# @FileName: 最大公约数.py
# @Author  : CNTian
# @Github  : https://github.com/CNPolaris
# @Email   ：1875091912@qq.com

def get(a,b):
    while b!=0:
        t=a%b
        a=b
        b=t
    return a
x=input()
y=input()
x_y=get(eval(x),eval(y))
xy=eval(x)*eval(y)/x_y
print("最大公约数为：{}，最小公倍数为：{}".format(x_y,xy))