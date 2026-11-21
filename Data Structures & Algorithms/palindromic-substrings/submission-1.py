class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        res = 0
        
        #odd
        for i in range(n):
            l, r = i, i

            while l>=0 and r <= n-1 and s[l] == s[r]:
                res+=1
                l-=1
                r+=1

        #even
        for i in range(n-1):
            l, r = i, i+1

            while l>=0 and r <= n-1 and s[l] == s[r]:
                res+=1
                l-=1
                r+=1

        return res
        

            
