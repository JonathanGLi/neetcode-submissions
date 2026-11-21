class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxLength = 0
        maxString = ""
        
        #odd
        n = len(s)

        for i in range(n):
            l, r = i, i
            length = -1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l-=1
                r+=1
                length += 2

            if length > maxLength:
                maxLength = length
                maxString = s[l+1: r]

        #even

        for i in range(n-1):
            l, r = i, i+1
            length = 0
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l-=1
                r+=1
                length += 2

            if length > maxLength:
                maxLength = length
                maxString = s[l+1: r]

        return maxString

