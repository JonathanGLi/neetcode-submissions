class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        # binary search
        #
        l = 0
        r = len(nums) -1

        while(l <= r):
            print("l", l, "r", r)


            m = (l+r)//2

            if (nums[m] == target) :
                return m
            #.    1 2 3 4 5
            elif (((nums[l] < nums[m]) and ((nums[l] <= target) and (target < nums[m]))) or
                    ((nums[l] > nums[m]) and ((nums[l] <= target) or (target < nums[m])))
                ):
                r = m - 1
            else:
                l = m+1

        return -1


