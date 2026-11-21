"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        

        sortedStarts = sorted([i.start for i in intervals])
        sortedEnds = sorted([i.end for i in intervals])

        s, e = 0, 0
        count = 0
        res = 0

        while s < len(sortedStarts):

            if sortedStarts[s] < sortedEnds[e]:
                s+=1
                count += 1
            else:
                e+= 1
                count-=1

            res = max(res, count)

        return res