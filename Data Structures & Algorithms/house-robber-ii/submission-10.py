class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        # 2 runs one with and one without

        n = len(nums)

        # max money starting from here
        def dfs(i, end):
            if i >= end:
                return 0

            if (i, end) in memo:
                return memo[(i, end)]

            memo[(i, end)] =  max(dfs(i+2, end) + nums[i], dfs(i+1, end))

            return memo[(i, end)]

        memo = {}

        a = dfs(0, n-1)

        memo = {}

        b = dfs(1, n)

        return max(a, b)


