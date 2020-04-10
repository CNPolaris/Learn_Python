# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 19:45
# @FileName: 4.2.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

def Calculation(num):
    s = sum(num)
    aver = s / len(num)
    return s, aver


res = []
s = input("输入一串整数数字（以空格作为分隔符）：")
n = s.split(' ')
for i in n:
    res.append(eval(i))
ans = res[0::3]

print(Calculation(res),ans)
#print(ans)
