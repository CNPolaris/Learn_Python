'''

1013.将数组分成和相等的三部分.py
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
'''
class Solution:
    def canThreePartsEqualSum(self, A):
        s = sum(A)#先计算A的和
        if s % 3 != 0: #如果无法分成三份就FALSE
            return False
        target = s // 3 #分成三等份作为目标
        n, i, cur = len(A), 0, 0
        while i < n:
            cur += A[i]
            if cur == target:
                break
            i += 1
        if cur != target:
            return False
        j = i + 1
        while j + 1 < n:  # 需要满足最后一个数组非空
            cur += A[j]
            if cur == target * 2:
                return True
            j += 1
        return False
test=Solution()
res=[0,2,1,-6,6,-7,9,1,2,0,1]
print(test.canThreePartsEqualSum(res))