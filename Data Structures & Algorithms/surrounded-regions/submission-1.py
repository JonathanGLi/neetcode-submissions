class Solution:
    def solve(self, board: List[List[str]]) -> None:

        marked = set()
        rows = len(board)
        cols = len(board[0])

        
        def dfs(i, j):
            if i <0 or i >= rows or j < 0 or j>= cols:
                return
            if board[i][j] == 'O' and (i, j) not in marked:
                marked.add((i, j))
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
                
            



        # loop through all borders
        # do dfs from that to mark all zeros as do not change
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)


        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)

        # change all other 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in marked:
                    board[r][c] = 'X'

