# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 8:23
# @FileName: 水仙花数.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris


def Daffodil():
    count = 0
    for n in range(100, 1000):
        a, b, c = map(int, str(n))
        if a ** 3 + b ** 3 + c ** 3 == n:
            count = count + 1
            print(n)
    print("三位数中的水仙花数", count)


if __name__ == '__main__':
    Daffodil()
