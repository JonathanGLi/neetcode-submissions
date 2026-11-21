class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        

        #bruteforce, dp + binary search

        # questions
        # empty array, negative profits

        # edge cases

        # nlogn, sorting and n dp calls, logn for binary search

        #zip together

        tuples = list(zip(startTime, endTime, profit))

        # sort by starttime
        tuples.sort(key = lambda t: t[0])

        n = len(startTime)

        cache = [-1] * n

        # dfs(i) -> max profit starting at index i, DP
        # i is the interval we are taking
        def dfs(i):

            # base case
            if i== n:
                return 0

            # use cache if cached
            if cache[i] != -1:
                return cache[i]

            #skip
            res = dfs(i+1)

            # binary search to find next valid interval after taking intervall i
            l, r = i+1, n-1
            j = n

            while l <= r:
                m = (l +r)//2
                #valid
                if tuples[m][0] >= tuples[i][1]:
                    j = m
                    r = m - 1
                else:
                    l = m + 1

            #take max
            res = max(res, dfs(j) + tuples[i][2])

            # cache sol
            cache[i] = res

            #return solution
            return res

        return dfs(0)



