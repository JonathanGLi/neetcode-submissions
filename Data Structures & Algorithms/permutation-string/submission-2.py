class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        refA = [0]*26
        A = [0]*26

        for c in s1:
            refA[ord(c) - ord("a")] += 1

        print("refA")
        print(refA)

        for i in range(len(s1)):
            A[ord(s2[i]) - ord("a")]+=1

        if refA == A:
            return True

        r = len(s1)

        while r != len(s2):
            print(A)
            l = r - len(s1)
            A[ord(s2[r]) - ord("a")]+=1
            A[ord(s2[l]) - ord("a")]-=1

            if refA == A:
                return True

            r+=1

        return False
        


        