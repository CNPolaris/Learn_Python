# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 8:23
# @FileName: 测试闰年.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris


def TestLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("{}是闰年".format(year))
    else:
        print("{}不是闰年".format(year))


if __name__ == '__main__':
    year = [2000, 2008, 3000, 2019]
    for num in year:
        TestLeapYear(num)
