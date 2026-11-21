class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        ROWS = len(heights)
        COLS = len(heights[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        # cost, r, c
        minheap = [(0, 0, 0)]

        map_coord_to_cost = {(0, 0) : 0}

        while minheap:
            cost, r, c = heapq.heappop(minheap)

            if (r, c) in map_coord_to_cost and map_coord_to_cost[(r, c)] < cost:
                continue

            if r == ROWS-1 and c == COLS-1:
                return cost

            for i, j in directions:
                r1 = r + i
                c1 = c + j

                if r1 >= 0 and r1 < ROWS and c1 >= 0 and c1 < COLS:
                    cost1 = max(cost, abs(heights[r][c] - heights[r1][c1]))

                    if (r1, c1) in map_coord_to_cost and map_coord_to_cost[(r1, c1)] <= cost1:
                        continue                    
    
                    map_coord_to_cost[(r1, c1)] = cost1
                    heapq.heappush(minheap, (cost1, r1, c1))










            