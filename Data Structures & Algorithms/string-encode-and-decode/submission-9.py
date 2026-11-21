class Solution:

    def encode(self, strs: List[str]) -> str:

        #["neet","code","love","you"] -> "4#neet4#code4#love3#you"]

        res = ""

        for s in strs:
            
            str1 = str(len(s)) + "#" + s

            res += str1

        return res

    def decode(self, s: str) -> List[str]:

        
        res = []
        i = 0

        while (i < len(s)):
            j = i

            while s[j]!= "#":
                j+=1
            
            length = int(s[i:j])

            i = j+1
            j = i + length
            
            word = s[i:j]

            res.append(word)

            i = j

        return res
