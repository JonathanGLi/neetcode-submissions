class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)

        res = []

        nums.sort()




        def dfs(i, cur):

            print((i, cur))

            if i >= n:
                res.append(cur.copy())
                return

            #try
            cur.append(nums[i])
            dfs(i+1, cur)
            
            #undo
            cur.pop()

            #while skip
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, cur)

            return

        dfs(0, [])

        return res

