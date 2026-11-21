class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        n = len(startTime)
        cache = [-1] * n
        index = list(range(n))
        index.sort(key = lambda i: startTime[i])

        def dfs(i):
            
            if i == n:
                return 0

            if cache[i] != -1:
                return cache[i]

            res = dfs(i+1)

            l = i+1
            r = n-1
            j = n

            while l <= r:
                mid = (l+r)//2
                if (startTime[index[mid]] >= endTime[index[i]]):
                    j = mid
                    r = mid-1
                else:
                    l = mid+1

            res = cache[i] = max(res, profit[index[i]] + dfs(j))

            return res

        return dfs(0)







