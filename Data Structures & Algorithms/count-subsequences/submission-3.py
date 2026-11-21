class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        # Questions 
        # contiguous? no
        # empty string? no

        #Edge cases


        #2 ways
        #brute force
        #2^len(s) and check if each one is eqal to cat

        #O(n * m), n = len(s), m = (len(t))

        #cache 2D matrix
        cache = [[-1 for _ in range(len(t))] for _ in range(len(s))]

        #dfs(i, j) -> number distinct subsequences from remaining letters
        def dfs(i, j):

            # if j = len(j), return 1
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            # if in cache, return cached value
            if cache[i][j] != -1:
                return cache[i][j]

            #res = 0
            res = 0
            if s[i] == t[j]:
                #res += if same, take and dp rest recur
                res += dfs(i+1, j+1)
                # res += or skip, recur
                res += dfs(i+1, j)
            else:
                # res = is diff, skip
                res += dfs(i+1, j)

            #save res to cache and return
            cache[i][j] = res

            return res

        return dfs(0, 0)







