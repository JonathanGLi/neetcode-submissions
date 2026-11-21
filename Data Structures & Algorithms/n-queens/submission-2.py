class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        resAll = []
        total = n * n 
        def solveOnce():

            rows = set()
            cols = set()
            diag1 = set()
            diag2 = set()
            coords = set()
        
            def dfs(c, idx_1):

                if c == n:
                    res = []
                    for r in range(n):
                        string = ""
                        for c in range(n):
                            if (r, c) in coords:
                                string += "Q"
                            else:
                                string += "."

                        res.append(string)
                    

                    resAll.append(res)

                    return

                #if (i not in rows) and (j not in cols) and (i-j not in diag1) and (i+j not in diag2):


                for idx in range(idx_1, total):
                    
                    i = idx//n
                    j = idx%n

                    if (i in rows) or (j in cols) or (i-j in diag1) or (i+j in diag2):
                        continue
                    
                    rows.add(i)
                    cols.add(j)
                    diag1.add(i-j)
                    diag2.add(i+j)
                    coords.add((i, j))

                    dfs(c+1, idx)

                    rows.remove(i)
                    cols.remove(j)
                    diag1.remove(i-j)
                    diag2.remove(i+j)
                    coords.remove((i, j))


            dfs(0, 0)



        solveOnce()

        return resAll

                    





