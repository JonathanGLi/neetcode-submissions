class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])


        q = deque()
        freshCount = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i, j])
                    grid[i][j] = 1

                if grid[i][j] == 1:
                    freshCount+=1

        freshCount2 = 0
        layer = 0
        res = 0
        while q:
            print(q)

            for _ in range(len(q)):
                [i, j] = q.popleft()
                if (i < 0 or i>= rows or j < 0 or j>= cols ):
                    continue
                
                if grid[i][j] == 1:
                    freshCount2 += 1
                    grid[i][j] = -1
                    q.append([i+1, j])
                    q.append([i-1, j])
                    q.append([i, j+1])
                    q.append([i, j-1])
                    res = layer

            layer+=1

        if freshCount != freshCount2:
            return -1
        return res








                