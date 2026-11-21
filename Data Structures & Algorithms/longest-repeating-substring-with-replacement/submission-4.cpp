class Solution {
public:
    int characterReplacement(string s, int k) {
        
        int i = 0, j = 0;
        int diff = 0;
        int maxFreq = 0;
        int maxWindowSize = 0;
        int windowSize = 0;

        unordered_map <char, int> freq;

        while (j < s.size()){
            freq[s[j]] += 1;
            maxFreq = max(maxFreq, freq[s[j]]);

            windowSize = j-i+1;
            diff = windowSize - maxFreq;
            
            if (diff > k) {
                freq[s[i]]-=1;
                i++;
            }
            maxWindowSize = max(maxWindowSize, j-i+1);

            j++;
        }

        return maxWindowSize;




    }
};
