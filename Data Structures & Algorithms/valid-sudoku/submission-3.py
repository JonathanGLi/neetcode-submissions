class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        l = 9

        for i in range(l):
            set1 = set()
            set2 = set()
            for j in range(l):

                if board[i][j] in set1:
                    return False
                if board[i][j] != ".":
                    set1.add(board[i][j])

                if board[j][i] in set2:
                    return False
                if board[j][i] != ".":
                    set2.add(board[j][i])

        for i1 in range(3):
            for j1 in range(3):
                set3 = set()
                for i2 in range(3):
                    for j2 in range(3):

                        cur = board[i1*3+i2][j1*3+j2]
            
                        if cur in set3:
                            return False
                        if cur != ".":
                            set3.add(cur)

        return True