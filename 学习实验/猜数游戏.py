#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/27 14:09
# @FileName: 猜数游戏.py
# @Author  : CNTian
# @Github  : https://github.com/CNPolaris
# @Email   ：1875091912@qq.com
import random

target = random.randint(0, 100)
n = input()
c = 0
while n != target:
    n=int(n)
    c += 1
    if type(n) != int:
        print("输入的内容必须是整数")
        n = input()
    elif n > target:
        print("遗憾，太大了")
        n = input()
    elif n < target:
        print("遗憾，太小了")
        n = input()
    elif n == target:
        print("预测{}次，你猜中了！".format(c))
        break
