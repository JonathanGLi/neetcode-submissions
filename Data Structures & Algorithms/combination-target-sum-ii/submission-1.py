class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        #RQE2

        #brute force, 2^n



        n = len(candidates)

        res = set()


        def dfs(i, total, arr):

            if i == n:
                if total == target:
                    res.add(tuple(sorted(arr)))
                return
            
            arr1 = arr.copy()
            arr1.append(candidates[i])
            dfs(i+1, total + candidates[i], arr1)

            dfs(i+1, total, arr)

            return 

        dfs(0, 0, [])

        return [list(t) for t in res]

            
                    