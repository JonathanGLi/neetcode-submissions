class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        longest_ending = defaultdict(int)
        longest = 0
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if longest_ending[j] + 1 > longest_ending[i]:
                        longest_ending[i] = longest_ending[j] + 1
                        longest = max(longest, longest_ending[j] + 1)

        return longest+1