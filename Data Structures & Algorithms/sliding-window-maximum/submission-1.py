class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        # (-val, index)
        maxHeap = []

        res = []

        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))


        for i in range(len(nums) - k + 1):

            while maxHeap[0][1] < i:
                heapq.heappop(maxHeap)

            res.append(-maxHeap[0][0])

            if i+k < len(nums):
                heapq.heappush(maxHeap, (-nums[i+k], i+k))



        return res



