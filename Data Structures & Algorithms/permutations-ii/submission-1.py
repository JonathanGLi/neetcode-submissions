class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        

        #n factorial
        # add to set then convert to list to remove dup
        nums.sort()
        counts = Counter(nums)

        n = len(nums)

        res = []


        def dfs(i, cur):
            if i == n:
                res.append(cur.copy())


            for k in counts.keys():
                
                if counts[k] > 0:
                    counts[k] -= 1

                    cur.append(k)
                    dfs(i+1, cur)
                    cur.pop()
                    counts[k] += 1

            return
        dfs(0, [])
        return res



            
                
