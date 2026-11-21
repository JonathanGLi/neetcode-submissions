class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      l, r = 0, 0
      maxx = 0
      cur = 0

      if len(s) == 0:
        return 0

      d = defaultdict(int)
      d[s[0]] += 1

      while r != len(s):
        cur = r-l+1
        maxx= max(maxx, cur)

        r+=1
        if r == len(s):
          break
        d[s[r]]+=1
      
        while l<r and d[s[r]]>1:
          d[s[l]]-=1
          l+=1

        print(d)

      return maxx





