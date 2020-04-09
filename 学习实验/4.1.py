# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 19:09
# @FileName: 4.1.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
import collections

N = input()
res = collections.Counter(N)
ans = res.keys()
sum = 0
for i in ans:
    sum += eval(i)
print(sum)
