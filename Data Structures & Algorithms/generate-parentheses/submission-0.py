class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        if n == 0:
            return []

        elif n == 1:
            return ["()"]


        else: 
            res = ["()"]
            for i in range(2, n+1):
                new = []
                for j in range(len(res)):
                    m = res.pop()
                    for k in range(len(m)+1):
                        a = m[:k] + "()" + m[k:]
                        new.append(a)

                res = list(set(new))

        return res

        

