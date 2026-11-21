class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        

        //xx
        if (s.length() == 0) {
            return 0;
        }

        //char->count
        unordered_map<char, int> map;

        int l = 0, r = 0;
        map[s[0]] = 1;

        int maxLen = 1;

        while (r < s.length()-1) {
            r++;
            map[s[r]]++;

            while(map[s[r]] > 1) {
                map[s[l]]--;
                l++;
            }

            maxLen = max(maxLen, r - l + 1);

        }

        return maxLen;
    }
};
