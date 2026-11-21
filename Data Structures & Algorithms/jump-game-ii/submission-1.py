class Solution:
    def jump(self, nums: List[int]) -> int:
        
        #n, n
        # dp

        memo = [-1 for i in range(len(nums)) ]

        def dfs(i):
            if i >= len(nums)-1:
                return 0

            if memo[i] != -1:
                return memo[i]

            minn = len(nums)
            #try all jumping options
            for j in range(nums[i]):
                jumpToIdx = i + j + 1
                minn = min(minn, dfs(jumpToIdx) + 1)

            memo[i] = minn

            return minn

        return dfs(0)