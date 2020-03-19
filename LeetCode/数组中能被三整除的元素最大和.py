'''
给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
'''
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted(nums)
        if sum(nums)%3==0:
            return nums
        elif sum(nums)%3==1 :
            nums=list(filter(lambda x:x%3!=1,nums))
        elif sum(nums) % 3 == 2:
            nums = list(filter(lambda x: x % 3 != 2, nums))
        return sum(nums)
test=Solution()
nums = [3,6,5,1,8]
print(test.maxSumDivThree(nums))
