class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

    //empty

    if (nums.size() == 0) {
        return 0;
    }
    //put all number in set

    unordered_set<int> s(nums.begin(), nums.end());

    int longest = 0;

    //loop through numbers
    for (int n : nums) {


        //if potenital start
        if (s.find(n - 1) == s.end()) {

            int count = 0;

            int x = n;
            
            while (s.find(x) != s.end()) {
                count ++;
                x++;
            }

            longest = max(count, longest);
        }

    }

    return longest;

    }
};
