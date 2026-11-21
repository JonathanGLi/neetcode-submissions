class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def dfs(s, i):

            if i == len(nums):
                if s == 0:
                    return 1
                else:
                    return 0

            if (s, i) in dp:
                return dp[(s, i)]

            add = dfs(s+nums[i], i+1)
            sub = dfs(s-nums[i], i+1)

            return add + sub

        return dfs(-target, 0)