class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = [-1 for i in range( len(nums))]

        def dfs(i):
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]

            rob = dfs(i+2) + nums[i]
            skip = dfs(i+1)

            res= max(rob, skip)

            memo[i] = res

            return res

        return dfs(0)


            



