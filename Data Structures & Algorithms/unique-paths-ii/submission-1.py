class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        

        #Store a negative 
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0

        # stores num paths from grid to end
        memo = [0] * COLS

        memo[COLS-1] = 1

        for r in range(ROWS - 1, -1, -1):  
            for c in range(COLS - 1, -1, -1): 

                # if obsticcal
                if obstacleGrid[r][c]:
                    memo[c] = 0
                elif c < COLS - 1:
                    memo[c] += memo[c+1] 

        return memo[0]