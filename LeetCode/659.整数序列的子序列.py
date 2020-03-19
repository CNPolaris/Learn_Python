'''
659输入一个按升序排序的整数数组（可能包含重复数字），
你需要将它们分割成几个子序列，其中每个子序列至少包含三个连续整数。
返回你是否能做出这样的分割？
'''
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<6:
            return False


#测试                 预期
num=[1,2,3,3,4,5]     #true
#num=[1,2,3,3,4,4,5,5] #true
#num=[1,2,3,4,4,5]     #true
test=Solution()
print(test.isPossible(num))
print(1<=2)

