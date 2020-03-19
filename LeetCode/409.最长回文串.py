'''
409.最长回文子串
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:假设字符串的长度不会超过 1010。
'''
import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0::]==s[::-1]:
            return len(s)
        sum=0
        res=collections.Counter(s)#计数器 返回字符串中元素及出现次数
        for i in res.values():#values 是返回出的出现次数
            sum+=i//2*2 #每个元素能最多使用次数
            if sum%2==0 and i%2!=0:#找一个可以在中间做回文数
                sum+=1
        return sum

str="a"
#str="bccccdd"
print(str[0::])
print(str[::-1])
test=Solution()
print(test.longestPalindrome(str))

