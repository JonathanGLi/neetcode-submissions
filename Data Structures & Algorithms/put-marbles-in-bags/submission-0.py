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

        minHeap = []
        maxHeap = []


        for x in pairSums:

            heapq.heappush(minHeap, x)
            heapq.heappush(maxHeap, -x)

        print(minHeap, maxHeap)
        minPairs = []
        maxPairs = []

        for i in range(k-1):
            minPairs.append(heapq.heappop(minHeap))
            maxPairs.append(heapq.heappop(maxHeap))

        print(minPairs, maxPairs)

        minHeapSum = weights[0] + weights[len(weights)-1]
        for x in minPairs:
            minHeapSum += x

        maxHeapSum = weights[0] + weights[len(weights)-1]
        for x in maxPairs:
            maxHeapSum -= x

        return maxHeapSum - minHeapSum

        