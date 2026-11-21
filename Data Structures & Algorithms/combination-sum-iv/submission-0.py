class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = defaultdict(int)

        # 0, 0
        # 1, 0
        # 2, 0
        # 3, 0 - 


        def dfs(total):


            if total == target:
                return 1
            elif total >= target:
                return 0

            if (total) in memo:
                return memo[(total)]

            for n1 in nums:
                memo[total] += dfs(total+n1)

            return memo[total]

        res = dfs(0)

        
        return res
            