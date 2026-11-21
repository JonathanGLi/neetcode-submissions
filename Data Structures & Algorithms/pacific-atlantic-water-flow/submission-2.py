class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ROWS = len(heights)
        COLS = len(heights[0])

        #dp can this cell reach pacific
        #0 not visited
        # 1 can reach pacific
        # 2 cannot reach pacific
        memo_pacific = [[0] * COLS for _ in range(ROWS)]
        
        #dp can this cell reach atlantic
        memo_atlantic = [[0] * COLS for _ in range(ROWS)]



        def dfs(r, c, memo):

            if (r, c) in visited:
                return 
            visited.add((r, c))

            memo[r][c] = 1

            for i, j in dirs:
                new_r, new_c = r + i, c + j

                # in bounds
                if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS:
                    continue

                #valid height
                if heights[new_r][new_c] < heights[r][c]:
                    continue

                dfs(new_r, new_c, memo)


        res = []

        for r in range(ROWS):
            for c in range(COLS): 

                if r == 0 or c == 0:
                    visited = set()
                    dfs(r, c, memo_pacific)

                if r == ROWS-1 or c == COLS-1:
                    visited = set()
                    dfs(r, c, memo_atlantic)

        for r in range(ROWS):
            for c in range(COLS): 
                if memo_pacific[r][c] and memo_atlantic[r][c]:
                    res.append([r, c])



        return res














