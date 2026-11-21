class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        

        total = sum(nums)

        if total % k != 0:
            return False


        bucketSize = total // k

        nums.sort(reverse = True)

        # set of used indecies
        used = [False] * len(nums)

        memo = {}

        def dfs(s, i, k):

            if (s, i, k) in memo:
                return memo[(s, i, k)]

            if k == 0:
                return True

            if s == bucketSize:
                return dfs(0, 0, k-1)

            for j in range(i, len(nums)):

                if used[j] or s + nums[j] > bucketSize:
                    continue

                used[j] = True

                if dfs(s + nums[j], j+1, k):
                    memo[(s, i, k)] = True
                    return True

                used[j] = False

            memo[(s, i, k)] = False
            return False



        return dfs(0, 0, k)

                



                

                














