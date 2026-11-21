class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        def foo(arr):
            
            arr[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                arr[i] = max(arr[i-1], arr[i] + arr[i-2])

            return arr[len(arr)-1]

        return max(foo(nums[1:]), foo(nums[:len(nums)-1]))