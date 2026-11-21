class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()

        res = []

        prev_i = float('inf')
        for i in range(len(nums)-3):
            if nums[i] == prev_i:
                continue
            prev_j = float('inf')
            for j in range(i+1, len(nums)-2):
                if nums[j] == prev_j:
                    continue
                l = j+1
                r = n-1
                t = target - nums[i] - nums[j]

                while l < r:
                    if nums[l] + nums[r] == t:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l+=1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
                    elif nums[l] + nums[r] < t:
                        l += 1
                    elif nums[l] + nums[r] > t:
                        r -= 1

                prev_j = nums[j]
            prev_i = nums[i]

        return res

        
                