class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        res = [0] * (len(num1) + len(num2))
        

        if num1 == '0' or num2 == '0':
            return "0"

        for i in range(len(num1)-1, -1, -1): 
            for j in range(len(num2)-1, -1, -1): 

                res [i + j+1] += int(num1[i]) * int(num2[j])

        print(res)

        for i in range(len(res)-1, -1, -1): 
            print(res[i])
            if i > 0:
                res[i-1] += res[i] // 10

            if res[i] > 0:
                res[i] = res[i] % 10
            res[i] = str(res[i])

        print(res)

        i = 0
        while res[i] == '0':
            i+=1

        print(res[i:])

        a = "".join(res[i:])

        print(a)

        return a        





                
