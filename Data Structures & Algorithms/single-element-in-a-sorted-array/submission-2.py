class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        

        # binary search

        #if we are at the first of a pair and the index is even then the answer is to the right

        #[3,3,7,7,10,11,11]
        #0, 6 => 3
        



        l, r = 0, len(nums)-1

        while l< r:
            m = (l+r)//2

            if m & 1:
                m-=1

            if nums[m] != nums[m+1]:
                r = m
            else:
                l = m + 2

        return nums[l]


