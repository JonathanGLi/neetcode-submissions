class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        if len(s2) < len(s1):
            return False 
        m1 = defaultdict(int)
        for c in s1:
            m1[c] += 1

        m2 = defaultdict(int)
        for i in range(len(s1)):
            m2[s2[i]] += 1

        i, j = 0, len(s1)

        while j < len(s2):

            print("m2", m2)
            
            if m1 == m2:
                return True


            m2[s2[j]] += 1
            m2[s2[i]] -= 1
            if m2[s2[i]] == 0:
                del m2[s2[i]]
            j+=1
            i+=1

        return m1 == m2