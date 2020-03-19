'''
711.宝石与石头
'''
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        s=0
        for i in J:
            s+=S.count(i)
        return s

test=Solution()
J = "aA"
S = "aAAbbbb"
print(test.numJewelsInStones(J,S))