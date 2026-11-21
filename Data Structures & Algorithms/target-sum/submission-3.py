class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        


        #dynamic
        memo = {}

        def dfs(i, sum):

            if (i, sum) in memo:
                return memo[(i, sum)]

            if i == len(nums):
                if sum == 0:
                    return 1
                else:
                    return 0

            res = dfs(i+1, sum+nums[i]) + dfs(i+1, sum - nums[i])

            memo[(i, sum)] = res
            return res
    

#1, 6      1, 2
#
        return dfs(0, target)