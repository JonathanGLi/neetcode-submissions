class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        #m^n
        width = len(t)
        height = len(s)

        matrix = [[0] * width for i in range(height)]

        for i in range(height):

            for j in range(width-1, -1, -1):

                if s[i] == t[j]:
                    if j == 0:
                        matrix[i][j] +=1

                    if i-1>=0 and j-1>=0:
                        matrix[i][j] += matrix[i-1][j-1]
                    if i-1>=0:
                        matrix[i][j] += matrix[i-1][j]

                else:
                    if i-1>=0:
                        matrix[i][j] = matrix[i-1][j]


        return matrix[height-1][width-1]