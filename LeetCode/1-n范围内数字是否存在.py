'''

'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=max(nums)+2
        res=set(range(n))
        for i in res:
            if i in nums:
                continue
            else:
                return i
test=Solution()
#num=[3,0,1]
num=[0]
print(test.missingNumber(num))