class Solution:
    def longestPalindrome(self, s: str) -> str:
        


        n = len(s)

        m, m_idx = 0, 0

        for i in range(n):
            l = r = i

            while l >=0 and r < n and s[l] == s[r]:
                l-=1
                r+=1
            l+=1
            r-=1
            if (r - l)+1 > m:
                m = (r - l)+1
                m_idx = l

        for i in range(n-1):
            l = i
            r = i+1

            while l >=0 and r < n and s[l] == s[r]:
                l-=1
                r+=1
            l+=1
            r-=1
            if (r - l)+1 > m:
                m = (r - l)+1
                m_idx = l

        return s[m_idx: m_idx + m]

            

            

            