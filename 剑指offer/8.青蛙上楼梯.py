#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/19 22:10
# @FileName: 8.青蛙上楼梯.py
# @Author  : CNTian
# @Github  : CNPolaris
# @Email   ：1875091912@qq.com
'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
'''
#青蛙爬楼梯
#python解法
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number in [1,2]:
            return number
        else:
            return self.jumpFloor(number-1)+self.jumpFloor(number-2)
#测试
test=Solution()
print(test.jumpFloor(5))
'''
//java版
public class Solution {
    public int JumpFloor(int target) {
    if (target==1)
        return 1;
    else if (target==2)
        return 2;
    else
        return JumpFloor(target-1)+JumpFloor(target-2);
    }
}
'''