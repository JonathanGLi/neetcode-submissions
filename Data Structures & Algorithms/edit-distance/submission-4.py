class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        #dp

        n = len(word1)
        m = len(word2)

        memo = {}

        def dfs(i, j):

            if i == n:
                return m - j
            elif j == m:
                return n - i

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = float('inf')
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i+1, j+1)
            else:
                memo[(i, j)] = min(memo[(i, j)], dfs(i, j+1), dfs(i+1, j), dfs(i+1, j+1)) + 1

            return memo[(i, j)]

        return dfs(0, 0)