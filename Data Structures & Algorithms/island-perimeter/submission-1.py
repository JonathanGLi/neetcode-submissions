class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        

        per = [0]
        visited = set()

        rows = len(grid)
        cols = len(grid[0])



        def dfs(i, j):

            print("dfs", i, j)

            if i < 0 or i >= rows or j < 0 or j >= cols:
                per[0] += 1
                return

            if grid[i][j] == 0:
                per[0] += 1
                return

            if (i, j) in visited:
                return
            
            visited.add((i, j))

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    print(i, j)
                    dfs(i, j)
                    return per[0]

