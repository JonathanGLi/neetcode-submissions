class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        # 0 1 0 0 0
        # 0 0 0 S 0
        # 0 S 1 0 1
        # 0 0 0 S 0
        # 0 0 0 0 0

        #[1,0,2,0,1]
        #[0,0,0,0,0]
        #[0,0,1,0,0]

        #for each node
            # bfs from every node
            # sum up the distance to each house

            # update max

        #return max


        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])

        empty_val = 0

        #total matrix for keeping track of sums
        total = [[0] * cols for _ in range(rows)]

        res = float('inf')

        for r in range(rows):
            for c in range(cols):   

                # BFS from house
                if grid[r][c] == 1:
                    #reset
                    res = float('inf')
                    steps = 0

                    levels = deque()
                    levels.append((r, c))
                    while levels:
                        steps += 1

                        for i in range(len(levels)):

                            coord = levels.popleft()

                            for dir in directions:
                                r1 = coord[0] + dir[0]
                                c1 = coord[1] + dir[1]

                                if (r1 >=0 and r1 < rows
                                    and c1 >=0 and c1 < cols
                                    and grid[r1][c1] == empty_val):

                                    grid[r1][c1] -= 1
                                    total[r1][c1] += steps
                                    levels.append((r1, c1))
                                    res = min(res, total[r1][c1])
                    empty_val -= 1

        return -1 if res == float('inf') else res























