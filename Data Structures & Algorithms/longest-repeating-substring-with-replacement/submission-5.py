class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        m = defaultdict(int)

        char = "A"
        char_count = 0 
        maxlen = 0
        max_freq = 0

        i, j = 0, 0

        while j < len(s):
            m[s[j]] += 1

            #updates to new char
            if s[j] != char and m[s[j]] > char_count:
                char = s[j]
                char_count = m[s[j]]
            max_freq = max(max_freq, m[char])

            #if cur_k too big, increase i
            while j-i - max_freq + 1 > k:
                m[s[i]] -= 1
                i+=1
            maxlen = max(maxlen, j - i + 1)
            j+=1
        return maxlen
        