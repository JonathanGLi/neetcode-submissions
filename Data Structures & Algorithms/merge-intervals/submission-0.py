class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        #nlogn bc sort and n space because res <= intervals
        sortedInt = sorted(intervals)

        res = []

        curStart = sortedInt[0][0]
        curEnd = sortedInt[0][1]
        for start, end in sortedInt:


            # attach to prev interval
            if start <= curEnd:
                curEnd = max(curEnd, end)
            #save prev interval and start new interval
            else:
                res.append([curStart, curEnd])
                curStart, curEnd = start, end

        res.append([curStart, curEnd])

        return res


