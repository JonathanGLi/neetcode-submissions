class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                
                cur = board[i][j]

                if cur != ".":

                    if cur in rows[i]:
                        return False
                    if cur in cols[j]:
                        return False
                    if cur in squares[3 * (i//3) + j//3]:
                        return False

                rows[i].add(cur)
                cols[j].add(cur)
                squares[3 * (i//3) + j//3].add(cur)

        return True
