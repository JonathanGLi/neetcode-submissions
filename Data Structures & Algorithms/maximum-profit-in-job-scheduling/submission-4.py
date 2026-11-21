class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        #(1, 5), (3, 5), (1, 5), (3, 5)
        #
        times = zip(endTime, startTime, profit)
        times = sorted(times)

        memo = {}

        #DP n^2, n^2

        def dfs(curTime, i):
            if i >= len(startTime):
                return 0
            if (curTime, i) in memo:
                return memo[(curTime, i)]


            # add
            add = 0
            #start, end = times[i][0], times[i][1]
            end, start = times[i][0], times[i][1]
            if start >= curTime:
                add = dfs(end, i+1) + times[i][2]

            # no add
            noAdd = dfs(curTime, i+1)

            res = max(add, noAdd)
            memo[(curTime, i)] = res

            return res
        


        return dfs(0, 0)







