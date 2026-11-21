class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []


        def backtrack(o, c, s):
            
            if (o + c == 2*n):
                res.append(s)

            if (o < n):
                backtrack(o+1, c, s+"(")
            if (c < o):
                backtrack(o, c+1, s+")")

        backtrack(0, 0, "")

        return res