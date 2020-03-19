'''
1071. 字符串的最大公因子
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
'''
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1+str2!=str2+str1:
            return ""
        differ=len(str1)-len(str2)
        if differ==0:return str1
        elif differ>0:
            str1=str1[len(str2):len(str1)]
        else:
            str2=str2[len(str1):len(str2)]
        return self.gcdOfStrings(str1,str2)