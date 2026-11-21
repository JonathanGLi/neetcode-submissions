class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        


        res = []


        def dfs(i, l):


            # if add:
            #     res.append(l)

            if i >= len(nums):
                res.append(l)
                return

            l1 = l.copy()   
            l2 = l.copy()
            l2.append(nums[i])   
            dfs(i+1, l1)

            dfs(i+1, l2)

        dfs(0, [])

        return res