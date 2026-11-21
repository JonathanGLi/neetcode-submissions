class Solution:
    def rob(self, nums: List[int]) -> int:

        print(nums[1:])

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        def foo(arr):
            
            a, b = 0, 0

            for x in arr:
                print(a, b)
                temp = max(x + a, b)
                a = b
                b = temp

            return b

        return max(foo(nums[1:]), foo(nums[:len(nums)-1]))