class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        longest_starting = defaultdict(int)
        longest = 0
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j] and longest_starting[i] < longest_starting[j]+1:
                    print(i, j)
                    longest_starting[i] = longest_starting[j]+1
                    longest = max(longest, longest_starting[j]+1)


        return longest+1