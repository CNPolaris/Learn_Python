# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 14:20
# @FileName: 随机数的二分查找.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
from numpy import *


def creatNum():
    num = random.randint(100, size=100)
    return num


def binarySearch(target, res):
    left = 0
    right = len(res) - 1
    while left <= right:
        mid = left + (right - left) //2
        if target < res[mid]:
            right = mid - 1
        elif target > res[mid]:
            left = mid + 1
        elif target == res[mid]:
            return mid
    return -1


if __name__ == '__main__':
    res = creatNum()
    res = sort(res)
    print(res)
    n= binarySearch(10,res)
    if n!=-1:
        print("位置在{}".format(n))
    else:
        print("不存在")
