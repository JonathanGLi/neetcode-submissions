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

        
        #actual solution
        memo = defaultdict(bool)


        def dfs(i, curSum):
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            if curSum == half:
                return True
            if curSum > half:
                return False
            if i >= len(nums):
                return False

            #skip
            skip = dfs(i+1, curSum)
            if skip == True:
                return True

            #take
            take = dfs(i+1, curSum + nums[i])
            if take == True:
                return True

            memo[(i, curSum)] = False

            return False

        return dfs(0, 0)
