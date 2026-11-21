class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def p(i, j):

            if i>= j:
                return
            mid = (int)((i+j) / 2)
            cand = [(nums[i], i), (nums[mid], mid), (nums[j], j)]
            cand.sort()
            p_idx = cand[1][1]
            pivot = nums[p_idx]

            nums[i], nums[p_idx] = nums[p_idx], nums[i]


            l = i+1
            r = j

            while l <= r:

                while l <= r and nums[r] > pivot:
                    r-=1
                while l <= r and nums[l] <= pivot:
                    l+=1

                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]


            nums[i], nums[r] = nums[r], nums[i]

            p(i, r-1)
            p(r+1, j)

        
        p(0, len(nums)-1)

        return nums