class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        prev = defaultdict(list)
        longest_ending = defaultdict(int)
        longest = 0
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    prev[i].append(j)

        for i in range(len(nums)):
            for k in prev[i]:
                if longest_ending[k] + 1 > longest_ending[i]:
                    longest_ending[i] = longest_ending[k] + 1
                    longest = max(longest, longest_ending[k] + 1)

        return longest+1