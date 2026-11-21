class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        n = len(s)

        def dfs(i):

            if i == n:
                return 1

            if i in memo:
                return memo[i]


            if s[i] == '0':
                return 0
            
            memo[i] = dfs(i+1)

            if i < n - 1:
                x = int(s[i:i+2]) 
                if x <= 26:
                    memo[i] += dfs(i+2)

            return memo[i]

        return dfs(0)



