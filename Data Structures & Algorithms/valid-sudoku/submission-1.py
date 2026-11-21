class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(9):
            D = defaultdict(int)
            for c in range(9):
                n = board[r][c]
                if D[n] != 0:
                    return False

                if n != ".":
                    if (int(n)<1 or int(n)>9):
                        return False
                    else:
                        D[n] = 1

        for c in range(9):
            D = defaultdict(int)
            for r in range(9):
                n = board[r][c]
                if D[n] != 0:
                    return False

                if n != ".":
                    if (int(n)<1 or int(n)>9):
                        return False
                    else:
                        D[n] = 1

        for r1 in range(0, 9, 3):
            for c1 in range(0, 9, 3):
                D = defaultdict(int)
                for r2 in range(3):
                    for c2 in range(3):
                        n = board[r1+r2][c1+c2]
                        if D[n] != 0:
                            return False

                        if n != ".":
                            if (int(n)<1 or int(n)>9):
                                return False
                            else:
                                D[n] = 1

        return True







