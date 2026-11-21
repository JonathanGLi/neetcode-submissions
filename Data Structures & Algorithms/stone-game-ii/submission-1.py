class Solution:
    def stoneGameII(self, piles: List[int]) -> int:


        dp = {}

        def dfs(alice, i, M):
            if i == len(piles):
                return 0
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]

            res = 0 if alice else float("inf")
            total = 0
            for X in range(1, 2 * M + 1):
                if i + X > len(piles):
                    break
                total += piles[i + X - 1]
                if alice:
                    res = max(res, total + dfs(not alice, i + X, max(M, X)))
                else:
                    res = min(res, dfs(not alice, i + X, max(M, X)))

            dp[(alice, i, M)] = res
            return res

        return dfs(True, 0, 1)
        
        # n = len(piles)

        # memo = {}

        # # the max amount money the cur player can make more than the other player from this state onwards
        # def dfs(i, m):

        #     if i == n:
        #         return 0

        #     if (i, m) in memo:
        #         return memo[(i, m)]

        #     s = 0
        #     memo[(i, m)] = -float('inf')
        #     for x in range(1, 1+2 * m):
        #         j= i+x-1
        #         if j < n:
        #             s += piles[j]
                        
        #             memo[(i, m)] = max(memo[(i, m)], s - dfs(j+1, max(m, x)))

        #     return memo[(i, m)]

        # a = dfs(0, 1)
        # res = (sum(piles) - a) // 2 + a

        # return res
        #