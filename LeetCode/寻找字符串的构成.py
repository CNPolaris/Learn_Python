'''

'''
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res="QWER"
        n=len(s)
        t=0
        for i in res:
            if s.count(i)==n//4:
                print(i,s.count(i))

            else:
                print(i,s.count(i))
                t=t+int(n//4-s.count(i))
        return t