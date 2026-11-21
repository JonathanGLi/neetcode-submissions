class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        

        #dp

        memo = {}

        rows = len(grid)
        cols = len(grid[0])


        def dfs(i, j):

            if i == rows - 1 and j == cols -1:
                return grid[i][j]

            if (i, j) in memo:
                return memo[(i, j)]

            if i < rows-1 and j == cols-1:
                res = dfs(i+1, j) + grid[i][j]
                memo[(i, j)] = res
                return res
            if i == rows-1 and j < cols-1:
                res = dfs(i, j+1) + grid[i][j]
                memo[(i, j)] = res
                return res

            down = dfs(i+1, j) +  grid[i][j]
            right = dfs(i, j+1) +  grid[i][j]

            res = min(down, right)
            memo[(i, j)] = res

            return res

        return dfs(0, 0)




