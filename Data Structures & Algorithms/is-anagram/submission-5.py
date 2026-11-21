class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        L1= [0] * 26
        L2= [0] * 26

        for c in s:
            L1[ord(c) - ord("a")]+=1

        for c in t:
            L2[ord(c) - ord("a")]+=1

        return L1 == L2


