class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        half = sum(stones)//2

        memo = {}

        # return cloest we can get with this total up to this point
        def dfs(i, total):

            if total >= half or i == len(stones):
                return abs(total - (sum(stones) - total))

            if (i, total) in memo:
                return memo[(i, total)]

            #take
            memo[(i, total)] = min(dfs(i+1, total + stones[i]), dfs(i+1, total))

            return memo[(i, total)]

        return dfs(0, 0)
            