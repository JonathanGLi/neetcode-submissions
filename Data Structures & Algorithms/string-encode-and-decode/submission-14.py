class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            l = str(len(s))
            res += l + "#"
            res += s

        return res

    def decode(self, s: str) -> List[str]:

        res = []

        i, j = 0, 0

        while i < len(s):

            while s[j] != "#":
                j+=1

            size = int(s[i:j])

            a, b = j+1, j+1+size

            res.append(s[a: b])

            i, j = b, b

        return res


