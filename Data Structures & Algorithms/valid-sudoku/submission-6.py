class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            tracker = set()
            for c in range(cols):

                k = board[r][c]
                if k != ".":
                    if k in tracker:
                        return False
                    else:
                        tracker.add(k)

        for c in range(cols):
            tracker = set()
            for r in range(rows):

                k = board[r][c]
                if k != ".":
                    if k in tracker:
                        return False
                    else:
                        tracker.add(k)

        for c1 in range(0, cols, 3):
            for r1 in range(0, rows, 3):
                tracker = set()
                for r in range(c1, c1+3):
                    for c in range(r1, r1+3):

                        k = board[r][c]
                        if k != ".":
                            if k in tracker:
                                return False
                            else:
                                tracker.add(k)

            
        return True



