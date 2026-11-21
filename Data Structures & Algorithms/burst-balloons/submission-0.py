class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        n = len(nums)

        memo = defaultdict(int)

        def dfs(i, j):

            if i+1 == j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            for k in range(i+1, j):
                memo[(i, j)] = max(memo[(i, j)], dfs(i, k) + dfs(k, j) + nums[k] * nums[i] * nums[j])

            return memo[(i, j)]


        return dfs(0, n-1)


