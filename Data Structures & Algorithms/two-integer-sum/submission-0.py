class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        D = {}
        res = []

        for i in range(len(nums)):
            if nums[i] in D:
                res.append(D.get(nums[i]))
                res.append(i)
                return res
            else:
                D[target-nums[i]] = i
