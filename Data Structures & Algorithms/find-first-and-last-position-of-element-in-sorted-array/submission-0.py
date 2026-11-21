class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def first(i):
            if (nums[i] == target and (i-1 == -1 or nums[i-1] != target)):
                return True
            return False

        def last(i):
            if (nums[i] == target and (i+1 == len(nums) or nums[i+1] != target)):
                return True
            return False


        firstRes, lastRes = -1, -1

        l, r = 0, len(nums)

    
        while l < r:
            m = (l+r)//2
            if first(m):
                firstRes = m
                break
            elif nums[m] >= target:
                r = m
            else:
                l = m+1

        l, r = 0, len(nums)
        while l < r:
            print(l, r)
            m = (l+r)//2
            if last(m):
                lastRes = m
                break
            elif nums[m] > target:
                r = m
            else:
                l = m+1

        return [firstRes, lastRes]








