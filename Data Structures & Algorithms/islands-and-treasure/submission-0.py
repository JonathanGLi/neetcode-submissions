class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # bfs starting from each treasure chest

        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        q = deque([])
        visited = set()

        #add all threasure to q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

                    visited.add((r, c))

        #bfs from treasure and label

        dist = -1

        while q:
            dist += 1
            print(q)
            for _ in range(len(q)):

                r1, c1 = q.popleft()

                if grid[r1][c1] == 2147483647:
                    grid[r1][c1] = dist
                    print("r1, c1", r1, c1)
                    print(visited)
                for i, j in directions:
                    r2 = r1 + i
                    c2 = c1 + j


                    if r2 >=0 and r2 < ROWS and c2 >=0 and c2 < COLS:
                        if grid[r2][c2] == 2147483647:
                            print("r2, c2", r2, c2)
                            if (r2, c2) not in visited:
                                print("r2, c2", r2, c2)
                                visited.add((r2, c2))
                                q.append((r2, c2))

        return None















