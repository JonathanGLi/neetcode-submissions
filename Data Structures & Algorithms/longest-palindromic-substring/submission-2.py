class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #abaxabaxabb
        def manacher(s):

            t = "#" + "#".join(s) + "#"

            l, r = 0, 0
            n = len(t)
            p = [0] * n

            for i in range(n):

                if r > i:
                    p[i] = min(r - i, p[l + r - i])
                else:
                    p[i] = 0

                while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]):
                    p[i] += 1

                if i + p[i] > r:
                    l = i - p[i]
                    r = i + p[i]

            return p

        maxx, m_i = max([(v, i) for i, v in enumerate(manacher(s))])
        half = (m_i - maxx)//2
        return s[half : half+maxx]

                
       