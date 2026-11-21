class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        


        res = []


        def dfs(i, l, add):


            if add:
                res.append(l)

            if i >= len(nums):
                return 

            l1 = l.copy()   
            l2 = l.copy()
            l2.append(nums[i])   
            dfs(i+1, l1, False)

            dfs(i+1, l2, True)

        dfs(0, [], True)

        return list(res)