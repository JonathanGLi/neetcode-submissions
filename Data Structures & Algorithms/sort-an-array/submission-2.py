class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def pivotSort(i, j):
            if i >= j:
                return
            
            # Choose median of first, middle, last as pivot
            mid = (i + j) // 2
            candidates = [(nums[i], i), (nums[mid], mid), (nums[j], j)]
            candidates.sort()
            pivot_idx = candidates[1][1]  # Median index
            
            nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
            
            pivot = nums[i]
            l = i + 1
            r = j
            
            while l <= r:
                while l <= r and nums[l] <= pivot:
                    l += 1
                while l <= r and nums[r] > pivot:
                    r -= 1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
            
            nums[i], nums[r] = nums[r], nums[i]
            
            pivotSort(i, r - 1)
            pivotSort(r + 1, j)
        
        pivotSort(0, len(nums) - 1)
        return nums