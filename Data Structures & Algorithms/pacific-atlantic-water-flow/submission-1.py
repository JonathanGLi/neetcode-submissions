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

        for r in range(ROWS):
            for c in range(COLS): 
                if r == 0 or c == 0:
                    memo_pacific[r][c] = 1

        for r in range(ROWS):
            for c in range(COLS): 
                if r == ROWS-1 or c == COLS-1:
                    memo_atlantic[r][c] = 1



        def dfs(r, c, memo):

            if (r, c) in visited:
                return False
            visited.add((r, c))


            if memo[r][c] == 1:
                return True
            elif memo[r][c] == 2:
                return False

            for i, j in dirs:
                new_r, new_c = r + i, c + j

                # in bounds
                if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS:
                    continue

                #valid height
                if heights[new_r][new_c] > heights[r][c]:
                    continue

                if dfs(new_r, new_c, memo):
                    memo[r][c] = 1
                    return True

            memo[r][c] = 2
            return False


        res = []

        for r in range(ROWS):
            for c in range(COLS): 

                visited = set()
                a = dfs(r, c, memo_pacific)
                # a = False
                visited = set()
                b = dfs(r, c, memo_atlantic)

                if a and b:
                    res.append([r, c])



        return res














