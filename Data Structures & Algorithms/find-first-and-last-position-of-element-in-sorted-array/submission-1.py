class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start, end = -1, -1

        def isStart(i):
            return i == 0 or nums[i] != nums[i-1]

        def isEnd(i):
            return i == len(nums)-1 or nums[i] != nums[i+1]     


        l = 0
        r = len(nums)-1

        while (l<=r):
            m = (l+r)//2
            print("m1", m)

            if isStart(m) and nums[m] == target:
                start = m
                break
            elif nums[m] < target:
                l = m+1
                print("a")

            else:
                r = m-1
                print("b")          

        l = 0
        r = len(nums)-1

        while (l<=r):
            m = (l+r)//2
            print("m2", m)
            if isEnd(m) and nums[m] == target:
                end = m
                break
            elif nums[m] > target:
                r = m-1

            else:
                l = m+1

        return [start, end]




