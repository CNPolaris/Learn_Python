#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/27 14:53
# @FileName: 倒计时数码管绘制.py
# @Author  : CNTian
# @Github  : https://github.com/CNPolaris
# @Email   ：1875091912@qq.com

import turtle as t

# 打表 每个线管在那些数字情况下需要画
line1 = [2, 3, 4, 5, 6, 8, 9]
line2 = [0, 1, 3, 4, 5, 6, 7, 8, 9]
line3 = [0, 2, 3, 5, 6, 8, 9]
line4 = [0, 2, 6, 8]
line5 = [0, 4, 5, 6, 8, 9]
line6 = [0, 2, 3, 5, 6, 7, 8, 9]
line7 = [0, 1, 2, 3, 4, 7, 8, 9]


# 画一根线管
def drawline(draw):
    if draw:
        t.pendown()
    else:
        t.penup()
    t.fd(40)
    t.right(90)


t.pensize(10)
t.speed(5)
# 判断是否需要移动位置
def move(m):
    if m > 1:
        t.penup()
        t.fd(20)
    else:
        t.penup()
        t.goto(0, 0)


def draw(m, num):  # 根据数字绘制七段数码管
    # 一号线
    if num in line1:
        drawline(True)
    else:
        drawline(False)
    # 二号线
    if num in line2:
        drawline(True)
    else:
        drawline(False)
    # 三号线
    if num in line3:
        drawline(True)
    else:
        drawline(False)
    # 四号线
    if num in line4:
        drawline(True)
    else:
        drawline(False)
    # 转一下防止转圈
    t.left(90)
    # 五号线
    if num in line5:
        drawline(True)
    else:
        drawline(False)
    # 六号线
    if num in line6:
        drawline(True)
    else:
        drawline(False)
    # 七号线
    if num in line7:
        drawline(True)
    else:
        drawline(False)
    t.left(180)
    # 判断下一个位置
    move(m)


# 开始倒计时
if __name__ == '__main__':
    n = input()
    for i in range(eval(n), -1, -1):
        t.clear()
        for k in str(i):
            draw(i, eval(k))
        t.penup()
        t.goto(0, 0)
    t.right(90)
    t.fd(100)
    t.write("计时结束",False,'center',font=('arial',14,'normal'))
    t.fd(20)
    t.done()
