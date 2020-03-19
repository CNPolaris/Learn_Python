'''

'''
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sorted(arr)
        for i in range(len(arr)):
            if arr[i]==0 and arr.count(arr[i])<2:
                continue
            if arr[i]*2 in arr:
                return True
        return False

arr = [-2,0,10,-19,4,6,-8]
test=Solution()
print(test.checkIfExist(arr))