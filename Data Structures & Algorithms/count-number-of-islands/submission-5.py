class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        count = [0]
        

        def bfs(i, j):

            q = deque([(i, j)])

            while q:
                i, j = deque.popleft(q)

                if i < 0 or j < 0 or i == rows or j == cols:
                    continue
                elif grid[i][j] == "1":
                    grid[i][j] = "x"
                    q.append((i+1, j))
                    q.append((i-1, j))
                    q.append((i, j+1))
                    q.append((i, j-1))


            return 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count[0] += 1
                bfs(r, c)
                

        return count[0]

