class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        


        if (nums.size() == 0) {
            return 0;
        }


        unordered_set<int> s (nums.begin(), nums.end());
        int longest = 0;


        for (int n : nums) {
            if (s.find(n-1) == s.end()) {

                int x = n;
                int count = 0;

                while (s.find(x) != s.end()){
                    x++;
                    count++;
                }
                longest = max(longest, count);

            }
        }

        return longest;
    }
};
