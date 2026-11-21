class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        #time n, space n

        negStones = [-s for s in stones]

        heapq.heapify(negStones)

        while len(negStones) > 1:

            print(negStones)

            #larger stone
            y = -heapq.heappop(negStones)
            x = -heapq.heappop(negStones)

            if x == y:
                pass
            elif x < y:
                heapq.heappush(negStones, -(y-x))

            print("end", negStones)

        if len(negStones) > 0:
            return -negStones[0]
        else:
            return 0
