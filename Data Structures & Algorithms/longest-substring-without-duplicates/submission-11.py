class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        count = defaultdict(int)

        l, r = 0, 0

        max_len = 0
        cur_len = 0

        while r < len(s):

            count[s[r]] += 1
            cur_len +=1

            while count[s[r]] > 1:

                count[s[l]] -= 1
                l +=1 
                cur_len-=1

            max_len = max(max_len, cur_len)

            r+= 1

        return max_len

