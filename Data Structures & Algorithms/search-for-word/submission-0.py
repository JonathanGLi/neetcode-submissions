class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        rows = len(board)
        cols = len(board[0])

        def startFrom(r, c):
            visited = set()

            def dfs(r, c, i):

                if i == len(word):
                    return True
                    
                if (r, c) in visited:
                    return False

                if r < 0 or r >= rows or c < 0 or c >= cols:
                    return False

                if board[r][c] == word[i]:

                    visited.add((r, c))

                    if dfs(r+1, c, i+1):
                        return True
                    if dfs(r-1, c, i+1):
                        return True
                    if dfs(r, c+1, i+1):
                        return True
                    if dfs(r, c-1, i+1):
                        return True

                    visited.remove((r, c))

                return False


            return dfs(r, c, 0)
            


            


        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c]:
                    if startFrom(r, c):
                        return True

        return False
