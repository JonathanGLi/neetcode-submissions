class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #n^m n is the traget and m in len nums

        #9


        #2 7, 2, 5, 3, 1, 


        #9

        #7, 4, 3, 0

        #5 2 1 



        nums.sort()

        res = []

        def dfs(i, curSum, arr):

            if curSum == target:
                res.append(arr.copy())

            if curSum > target:
                return

            for j in range(i, len(nums)):
                arr.append(nums[j])
                dfs(j, curSum + nums[j], arr)
                arr.pop()
        arr = []
        dfs(0, 0, arr)

        return res




