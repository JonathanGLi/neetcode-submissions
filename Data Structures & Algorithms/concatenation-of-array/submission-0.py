class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        res = nums.copy()
        for c in nums:
            res.append(c)

        return res