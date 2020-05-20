# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 9:07
# @FileName: pandas库练习.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

'''
（1）创建DataFrame 对象salary
（2）添加列
（3）添加行
（4）删除第四行，注意delete和drop的区别。默认删除行，如何删除列？指定axis=1.
（5）将“tax”列的值统一修改为“0.03”
'''
from pandas import *
from pandas import *


# 创建
def createData():
    global res
    res = {"name": ["Mayue", "Lilin", "Wuyun"], "pay": [3000, 4500, 8000]}
    global salary
    salary = DataFrame(res)
    # print(salary)


# 添加列['tax']=[0.05,0.05,0.1]
def addColumnData():  # 为不存在的列赋值会创建新的列
    salary['tax'] = [0.05, 0.05, 0.1]
    # print(salary)


# 添加行
def addLineData():
    salary.loc[3] = {'name': 'Liuxi', 'pay': 5000, 'tax': 0.05}
    print(salary)


# 删除
def delLine():
    # 删除第四行
    # salary.drop(salary.index[3],inplace=True)
    # 删除第三列
    salary.drop(salary.columns[2], axis=1, inplace=True)
    print(salary)


# 修改
def updateData():
    salary.iloc[0:4,2]=0.03
    print(salary)
if __name__ == '__main__':
    createData()
    addColumnData()
    addLineData()
    #delLine()
    updateData()