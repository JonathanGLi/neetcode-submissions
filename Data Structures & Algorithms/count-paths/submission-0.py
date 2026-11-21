class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        mapp = [[0] * m for i in range(n)]

        mapp[0][0] = 1 

        for i in range(n):
            for j in range(m):
                
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    mapp[i][j] = mapp[0][j-1]
                elif j == 0:
                    mapp[i][j] = mapp[i-1][0]
                else:
                    mapp[i][j] = mapp[i-1][j] + mapp[i][j-1]

        return mapp[n-1][m-1]
                

