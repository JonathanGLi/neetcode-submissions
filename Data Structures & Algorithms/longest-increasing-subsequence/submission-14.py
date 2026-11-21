class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        n = len(nums)
        memo = {}


        def dfs(i):
            print('i', i)

            if i == n:
                return 0

            if i in memo:
                return memo[i]

            a = 0
            for j in range(n, i, -1):
                print('j', j)
                if j == n or nums[j] > nums[i]:
                    a = max(dfs(j)+1, a)
            memo[i] = a

            return memo[i]
        
        res = 0
        for i in range(n):
            res = max(dfs(i), res)

        return res


            