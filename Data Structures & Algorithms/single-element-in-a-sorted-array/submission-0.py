class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        

        # binary search

        #if we are at the first of a pair and the index is even then the answer is to the right

        #[3,3,7,7,10,11,11]
        #0, 6 => 3
        

        def toTheRight(i):
            if ((0 == i or nums[i-1] != nums[i]) 
            and (len(nums)-1 == i or nums[i+1] == nums[i])
            and (i %2 == 0)):
                return True

            if ((0 == i or nums[i-1] == nums[i]) 
            and (len(nums)-1 == i or nums[i+1] != nums[i])
            and (i %2 == 1)):
                return True

            return False
            



        l, r = 0, len(nums)

        while l< r:
            m = (l+r)//2

            if (0 == m or nums[m-1] != nums[m]) and (len(nums)-1 == m or nums[m+1] != nums[m]):
                return nums[m]

            elif toTheRight(m):
                l = m + 1

            else:
                r = m

        return -1


