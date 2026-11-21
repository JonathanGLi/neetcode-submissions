class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if len(nums) == 0:
            return 0

        l, r = 0, len(nums)-1

        print(l, r)

        while(l < r):
            print('aa')

            while (l < r and nums[l]!= val):
                l+=1
            while (l < r and nums[r]== val):
                r-=1

            print(l, r)

            if (l>= r):
                break

            nums[l], nums[r] = nums[r], nums[l]

            print(l, r)

        if nums[l] != val:
            l+= 1

        return l