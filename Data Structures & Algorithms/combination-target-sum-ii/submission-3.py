class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        #RQE2

        #brute force, 2^n


        candidates.sort()
        n = len(candidates)

        res = []


        def dfs(i, total, arr):

            if i == n:
                if total == target:
                    res.append(arr.copy())
                return
            
            arr.append(candidates[i])
            dfs(i+1, total + candidates[i], arr)
            arr.pop()

            while i +1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, total, arr)

            return 

        dfs(0, 0, [])

        return res

            
                    