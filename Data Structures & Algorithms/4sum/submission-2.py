class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()

        res = []

        prev_i = float('inf')
        print(nums)
        for i in range(len(nums)-3):
            print("nums[i], prev_i", nums[i], prev_i)
            if nums[i] == prev_i:
                continue
            prev_j = float('inf')
            for j in range(i+1, len(nums)-2):
                print("nums[j], prev_j", nums[j], prev_j)
                if nums[j] == prev_j:
                    continue
                print(i, j)
                l = j+1
                r = n-1
                t = target - nums[i] - nums[j]

                while l < r:
                    print(i, j, l, r)
                    if nums[l] + nums[r] == t:
                        print(i, j, l, r)
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

        
                