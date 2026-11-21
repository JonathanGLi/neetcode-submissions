class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}

        def dfs(i, j):
            # BC 2 left
            # return max - min
            if i + 1 == j:
                return abs(piles[i] - piles[j])

            if (i, j) in memo:
                return memo[(i, j)]

            # recur
            # 2 options
            # max(l + min(dfs - l, dfs - r), r + min(dfs - l, dfs - r)

            res = max(piles[i] + min(dfs(i+2, j) - piles[i+1], dfs(i+1, j-1) - piles[j]), 
            piles[j] + min(dfs(i, j-2) - piles[j-1], dfs(i+1, j-1) - piles[i]))

            memo[(i, j)] = res

            # return stones
            return res

        res = dfs(0, len(piles)-1)

        return res > 0