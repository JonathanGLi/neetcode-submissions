class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        l, r = 0, 0
        n = len(nums)

        summ = nums[0]
        res = float('inf')

        while True:

            while r<n-1 and summ < target:
                r+=1
                summ += nums[r]

            if r == n-1 and summ < target:
                break

            res = min(res, r - l + 1)

            summ -= nums[l]
            l += 1

        return 0 if res == float('inf') else res




