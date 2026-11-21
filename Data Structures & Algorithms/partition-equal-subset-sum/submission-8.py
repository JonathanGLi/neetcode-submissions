class Solution:
    def canPartition(self, nums: List[int]) -> bool:


        #find half
        summ = 0
        half = 0
        for n in nums:
            summ += n

        if summ%2 == 1:
            return False
        else:
            half = int(summ/2)

        print(half)
        
        #actual solution
        memo = defaultdict(bool)


        def dfs(i, need):
            print(i, need)
            if (i, need) in memo:
                return memo[(i, need)]
            if need == 0:
                return True
            if need < 0:
                return False
            if i < 0:
                return False

            #skip
            skip = dfs(i-1, need)

            #take
            take = dfs(i-1, need - nums[i])

            res = skip or take

            memo[(i, need)] = res

            return res

        return dfs(len(nums)-1, half)

