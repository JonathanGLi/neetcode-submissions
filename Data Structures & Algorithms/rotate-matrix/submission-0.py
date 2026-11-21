class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)

        for i in range((n+1)//2):
            for j in range(n//2):
                val = matrix[i][j]
                for _ in range(4):
                    r = j
                    c = n - i - 1
                    temp = matrix[r][c]
                    matrix[r][c] = val
                    val = temp
                    i, j = r, c


