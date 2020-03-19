'''
有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。
对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为本次查询的结果。
并返回一个包含给定查询 queries 所有结果的数组。
'''
queries = [[0,1],[1,2],[0,3],[3,3]]
arr = [1,3,4,8]
from functools import reduce
class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(queries)):
            L=queries[i][0]
            R=queries[i][1]
            if L==R:
                res.append(arr[R])
            else:
                res.append(reduce(lambda a,b:a^b,arr[L:R+1]))
        return res
def XOR(a,b):
    return a^b
test=Solution()
print(test.xorQueries(arr,queries))
print(1^3^4^8)