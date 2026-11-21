class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        

        #Store a negative 
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0

        # stores num paths from grid to end
        memo = [[0] * COLS for _ in range(ROWS)]

        memo[ROWS-1][COLS-1] = 1

        for r in range(ROWS - 1, -1, -1):  
            for c in range(COLS - 1, -1, -1): 

                # if no obsticcal
                if obstacleGrid[r][c] == 0:

                    print("============")
                    print(r, c, obstacleGrid[r][c])
                        
                    # sum up memo from down and right
                    if r < ROWS - 1:
                        memo[r][c] += memo[r+1][c] 

                    if c < COLS - 1:
                        memo[r][c] += memo[r][c+1] 

                    print(memo[r][c])
        # time = space = m x n

        return memo[0][0]