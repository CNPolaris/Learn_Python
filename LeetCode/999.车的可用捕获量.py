#!/usr/bin/python3
# -*-coding: utf-8 -*-
# @Time    : 2020/3/26 8:25
# @FileName: 999.车的可用捕获量.py
# @Author  : CNTian
# @Github  : https://github.com/CNPolaris
# @Email   ：1875091912@qq.com

'''
在一个 8 x 8 的棋盘上，有一个白色车（rook）。
也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。
它们分别以字符 “R”，“.”，“B” 和 “p” 给出。
大写字符表示白棋，小写字符表示黑棋。
车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），
然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。
另外，车不能与其他友方（白色）象进入同一个方格。
返回车能够在一次移动中捕获到的卒的数量。
'''

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        N=len(board)
        ans=0
        R_x,R_y=0,0
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        for i in range(N):
            for j in range(N):
                if board[i][j]=="R":
                    R_x,R_y=i,j
        '''
        for k in range(4):#上下左右
            step=0
            while True:
                tx=R_x+step*dx[k]
                ty=R_y+step*dy[k]
                if tx < 0 or tx >= 8 or ty < 0 or ty >= 8 or board[tx][ty] == "B":
                    break
                if board[tx][ty]=="p":
                    ans+=1
                    break
                step+=1
        '''
        #右
        for i in range(R_x,N):
            if i<0 or i>=8 or board[i][R_y]=="B":
                break
            if board[i][R_y]=="p":
                ans+=1
                break
        #左
        for i in range(R_x,-1,-1):
            if i<0 or i>=8 or board[i][R_y]=="B":
                break
            if board[i][R_y]=="p":
                ans+=1
                break
        #上
        for i in range(R_y,N):
            if i<0 or i>=8 or board[R_x][i]=="B":
                break
            if board[R_x][i]=="p":
                ans+=1
                break
        #下
        for i in range(R_y,-1,-1):
            if i<0 or i>=8 or board[R_x][i]=="B":
                break
            if board[R_x][i]=="p":
                ans+=1
                break
        return ans
test=Solution()
xy=[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
print(test.numRookCaptures(xy))