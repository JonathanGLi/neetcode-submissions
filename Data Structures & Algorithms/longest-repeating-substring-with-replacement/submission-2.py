class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0, 0
        d = defaultdict(int)
        maxLet = s[0]
        maxFreq = 0
        maxx = 0
        d[s[0]]+=1
        print("d[maxNum]: " + str(d[maxLet]))
        while r!= len(s):
            maxx = max(maxx, r-l+1)
            r+=1

            if r == len(s):
                break

            d[s[r]]+=1

            if d[s[r]] >= d[maxLet]:
                print("d[s[r]]: " + str(d[s[r]]))
                print("maxNum: " + str(maxLet))
                print("d[maxNum]: " + str(d[maxLet]))
                maxLet = s[r]
                if d[maxLet] > maxFreq:
                    maxFreq = d[maxLet]

            while (r-l+1 > maxFreq + k):
                d[s[l]]-=1
                l+=1

            print("l: " + str(l) + 
            ", r: " + str(r) + 
            ", maxNum: " + str(maxLet) + 
            ", maxFreq: " + str(maxFreq) + 
            ", maxx: " + str(maxx))

        return maxx



