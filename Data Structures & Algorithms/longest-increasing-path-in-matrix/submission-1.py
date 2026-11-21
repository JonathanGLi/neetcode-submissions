class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        #For each cell in double forloop
        #call dfs from that cell, getting the longest increasing path from that cell with cahced bfs
        #n^2 because go to each cell once

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        memo = {}

        ROWS = len(matrix)
        COLS = len(matrix[0])

        visited = set()

        def dfs(r, c):
            print("r, c", r, c, "===========")


            if (r, c) in memo:
                return memo[(r, c)]

            best_next_path_len = 0
            for i, j in directions:
                print("r, c, i, j", r, c, i, j)
                r1, c1 = r + i, c + j

                if r1 < 0 or r1 >= ROWS or c1 < 0 or c1 >= COLS:
                    continue

                if matrix[r1][c1] > matrix[r][c]:
                    print("r1, c1", r1, c1)

                    best_next_path_len = max(best_next_path_len, dfs(r1, c1))

            memo[(r, c)] = best_next_path_len + 1

            return memo[(r, c)]


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
    
        print(memo)

        return res

