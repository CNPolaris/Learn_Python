# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 23:26
# @FileName: 289. 生命游戏.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

'''
根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # board_copy = board   ##这种方式不对
        row = len(board)    ##行
        col = len(board[0]) ##列
        board_copy = [[board[rw][cl] for cl in range(col)] for rw in range(row)]
        ##定义八个方向:上，下，左，右，左上，左下，右上，右下
        direction = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1],[-1,1],[1,1]]
        for i in range(row):
            for j in range(col):
                nums = 0 ##记录八个方向上的活细胞或者死细胞的个数
                for k in range(8):
                    dx = direction[k][0]+i
                    dy = direction[k][1]+j
                    if dx>=0 and dx<row and dy>=0 and dy<col and board_copy[dx][dy]==1:
                        nums+=1

                if board_copy[i][j]==1:
                    if nums<2:
                        board[i][j] = 0
                    if nums>3:
                        board[i][j] = 0
                    if nums==2 or nums==3:
                        board[i][j] = 1
                else:
                    if nums==3:
                        board[i][j] = 1

'''
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
'''