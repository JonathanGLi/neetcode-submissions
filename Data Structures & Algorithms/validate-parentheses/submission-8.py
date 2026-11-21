class Solution:
    def isValid(self, s: str) -> bool:

        st = []

        d = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }
        #print("aa")

        for c in s:
            #print("c: " + c)

            if c in d: 
                if len(st) == 0 or st.pop() != d[c]:
                    return False
            else:
                st.append(c)

            #print("st: ", st)

        return len(st) == 0





        