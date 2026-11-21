class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        

        def dfs(i, j, k):
            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                else:
                    return False

            print("call")

            res = False

            if i < len(s1) and s1[i] == s3[k]:
                print("a")
                if dfs(i+1, j, k+1):
                    res = True
                    print("a")

            if j < len(s2) and s2[j] == s3[k]:
                print("b")
                if dfs(i, j+1, k+1):
                    res = True

            return res

        return dfs(0, 0, 0)