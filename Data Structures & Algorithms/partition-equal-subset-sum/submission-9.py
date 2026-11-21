class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 == 1:
            return False
        half = sum(nums)//2
        n = len(nums)

        memo = {}

        def dfs(i, total):
            print(i, total)

            if total == half:
                return True

            if total > half:
                return False

            if i >= n:
                return False

            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = dfs(i+1, total + nums[i]) or dfs(i+1, total)

            print(i, total, memo[(i, total)])

            return memo[(i, total)]

        return dfs(0, 0)


            
