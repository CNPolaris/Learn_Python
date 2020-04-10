# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:10
# @FileName: 4.3.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

name = {"张三": 88, "李四": 90, "王五": 73, "赵六": 82}
# 添加
name["钱七"] = 90
# 修改
name["王五"] = 93
# 删除
name.pop("赵六")
print(name)
