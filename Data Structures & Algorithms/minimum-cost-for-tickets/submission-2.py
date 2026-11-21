class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

        n = len(days)
        memo = [-1] * n

        # finds first integer greater than x
        def binarySearch(x, l):
            r = n-1
            res = n
            while l <= r:
                m = (l + r) // 2
                
                if days[m] >= x:
                    res = m
                    r = m - 1
                else:
                    l = m + 1

            return res


        # dp
        # n , n
        def dfs(i):

            print(i)

            if i >= n:
                return 0

            if memo[i] != -1:
                return memo[i]

            
            a = dfs(i+1) + costs[0]

            # j = i
            # while j < n and days[j] < days[i] + 7:
            #     j+=1

            j = binarySearch(days[i] + 7, i+1)
            b = dfs(j) + costs[1]


            # j = i
            # while j < n and days[j] < days[i] + 30:
            #     j+=1
            j = binarySearch(days[i] + 30, i+1)
            c = dfs(j) + costs[2]

            res = min(a, min(b, c))

            memo[i] = res

            return res

        return dfs(0)
            

