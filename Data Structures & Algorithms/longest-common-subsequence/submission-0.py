class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        l1 = len(text1)
        l2 = len(text2)

        mapp = [[0] * l2 for _ in range(l1)]


        for i in range(l1):
            for j in range(l2):

                add = 0
                #same
                if text1[i] == text2[j]:

                    if i == 0 and j ==0:
                        mapp[i][j] = 1
                    elif j ==0:
                        mapp[i][j] = 1
                    elif i == 0:
                        mapp[i][j] = 1
                    else:
                        mapp[i][j] =  mapp[i-1][j-1] + 1
                #not same
                else:
                    if i == 0 and j ==0:
                        mapp[i][j] = 0
                    elif j ==0:
                        mapp[i][j] = mapp[i-1][j]
                    elif i == 0:
                        mapp[i][j] = mapp[i][j-1]
                    else:
                        mapp[i][j] = max(mapp[i-1][j], mapp[i][j-1])

        return mapp[l1-1][l2-1]

        