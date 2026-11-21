class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0, 0
        d = defaultdict(int)
        maxNum = 0
        maxx = 0
        d[s[0]]+=1

        while r!= len(s):
            maxx = max(maxx, r-l+1)
            r+=1

            if r == len(s):
                break

            d[s[r]]+=1

            if d[s[r]] > d[maxNum]:
                maxNum = s[r]

            while (r-l+1 > (d[maxNum] + k)):
                d[s[l]]-=1
                for k1, v1 in d.items():
                    if v1> d[maxNum]:
                        maxNum = k1
                l+=1

        return maxx



