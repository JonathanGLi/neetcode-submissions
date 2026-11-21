class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        

        # find the min double pairst

        # find the max double pairs

        #[5, 7, 9, 5]
        #[12, 16, 14]
        #[0, 1, 2]

        #

        #(sum, index)
        pairSums = [weights[i] + weights[i+1] for i in range(len(weights)-1)]

        print(pairSums)

        maxNums_Heap = []
        minNums_Heap = []


        for x in pairSums:

            heapq.heappush(maxNums_Heap, x)
            if len(maxNums_Heap) > k-1:
                heapq.heappop(maxNums_Heap)

            heapq.heappush(minNums_Heap, -x)
            if len(minNums_Heap) > k-1:
                heapq.heappop(minNums_Heap)


        print(maxNums_Heap, minNums_Heap)

        maxHeapSum = weights[0] + weights[len(weights)-1]
        maxHeapSum += sum(maxNums_Heap)

        minHeapSum = weights[0] + weights[len(weights)-1]
        minHeapSum -= sum(minNums_Heap)


        return maxHeapSum - minHeapSum

        