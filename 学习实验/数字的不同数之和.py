# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 14:46
# @FileName: 数字的不同数之和.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

import collections
N = input()
ans = collections.Counter(N)
res = ans.keys()
sum = 0
for i in res:
    sum += eval(i)
print(sum)
