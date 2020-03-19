'''

'''
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        b = n // 4
        from collections import Counter
        counter = Counter(s)
        counter = {key: value for key, value in counter.items() if value > b}

        if not counter or n < 4:
            return 0
        rmove = True

        l, r = 0, 0
        minlen = n

        while l <= r and r < n:

            if s[r] in counter and rmove:
                counter[s[r]] -= 1
            elif l > 0 and s[l - 1] in counter and not rmove:
                counter[s[l - 1]] += 1

            if {key: value for key, value in counter.items() if value > b}:
                r += 1
                rmove = True
            else:
                minlen = min(minlen, r - l + 1)
                l += 1
                rmove = False

        return minlen
test=Solution()
s = "QQQW"
print(test.balancedString(s))