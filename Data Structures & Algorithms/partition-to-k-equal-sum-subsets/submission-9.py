# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        

#         total = sum(nums)

#         if total % k != 0:
#             return False


#         bucketSize = total // k

#         nums.sort(reverse = True)

#         # set of used indecies
#         used = [False] * len(nums)

#         def dfs(s, i, k):

#             if k == 0:
#                 return True

#             if s == bucketSize:
#                 return dfs(0, 0, k-1)

#             for j in range(i, len(nums)):

#                 if used[j] or s + nums[j] > bucketSize:
#                     continue

#                 used[j] = True

#                 if dfs(s + nums[j], j+1, k):
#                     return True

#                 used[j] = False

#             return False



#         return dfs(0, 0, k)

                



                

                

















class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            return False

        return backtrack(0, k, 0)
