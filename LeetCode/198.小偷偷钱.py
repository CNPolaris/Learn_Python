'''
198你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        t=nums[0]
        sum=max(nums[0:2])
        for i in range(2,len(nums)):
            next=max(t+nums[i],sum)
            t=sum
            sum=next
        return sum

test=Solution()
#num=[1,2,3,1]
#num=[2,7,9,3,1]
#num=[2,1,1,2]
#num=[]
#num=[1,2]
num=[2,4,2]
print(test.rob(num))
