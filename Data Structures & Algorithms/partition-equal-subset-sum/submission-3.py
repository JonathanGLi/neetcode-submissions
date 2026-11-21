class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        #find half
        summ = 0
        half = 0
        for n in nums:
            summ += n

        if summ%2 == 1:
            print("hi")
            return False
        else:
            half = int(summ/2)

        
        #actual solution
        N = len(nums)
        memo = [[False] * (summ+1) for _ in range(N)]

        #fill first col with 0
        for i in range(N):
            memo[i][0] = True

        for i in range(N):
            for curSum in range(half+1):
                skip = memo[i-1][curSum]
                take = memo[i-1][curSum - nums[i]]
                memo[i][curSum] = skip or take


        res = memo[N-1][half]

        def printTable():
            for i in range(N):
                print(memo[i])
        printTable()
            
        return res

