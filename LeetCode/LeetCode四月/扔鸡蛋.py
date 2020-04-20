# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 20:33
# @FileName: 扔鸡蛋.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
'''
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。0
每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
你的目标是确切地知道 F 的值是多少。
无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
'''
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [0] * (K + 1)
        m = 0
        while dp[K] < N:
            m += 1
            for k in range(K, 0, -1):
                # print(m, k)
                dp[k] = dp[k - 1] + dp[k] + 1
        return m