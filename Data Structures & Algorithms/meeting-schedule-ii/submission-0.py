"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        


        #sort by start time 

        # max heap

        #(0)

        #40
        #loop through intervals
        # while the start time is smaller than the current time of the current index of the maxheap, increment the index of the max heap
        #retunr the size fo the maxheap

        # nlogn n


        sortedIntervals = sorted([(i.start, i.end) for i in intervals])
        minHeap = []

        for start_time, end_time in sortedIntervals:
            i = 0
            while i < len(minHeap) and minHeap[i] > start_time:
                i += 1

            if i == len (minHeap):
                heapq.heappush(minHeap, end_time)
            else:
                minHeap[i] = end_time
                heapq.heapify(minHeap)

        return len(minHeap)


            



