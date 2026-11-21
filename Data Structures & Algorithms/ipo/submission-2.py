class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        




        # sort (profits, captital) array largest profits first

        # k times
        # find the largest profit you acan affor 


        maxProfits = []

        minCapital = [(c, p) for c, p in zip(capital, profits)]

        heapq.heapify(minCapital)


        for i in range(k):

            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfits, -p)

            if not maxProfits:
                return w

            p = heapq.heappop(maxProfits)
            w -= p


        return w



            

