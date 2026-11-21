class Solution {
public:
    int longestConsecutive(vector<int>& nums) {


        //maps (needed start, needed end ) to length
        if (nums.empty()) {
            return 0;
        }

        // 1. Put all numbers into a hash set for O(1) lookups
        std::unordered_set<int> num_set(nums.begin(), nums.end());
        int longest_streak = 0;

        // 2. Iterate through each number in the set
        for (int num : num_set) {
            // 3. Check if it's the start of a sequence
            // If num-1 is not in the set, then num is a potential start
            if (num_set.find(num - 1) == num_set.end()) {
                int current_num = num;
                int current_streak = 1;

                // 4. Count the length of the sequence starting from num
                while (num_set.find(current_num + 1) != num_set.end()) {
                    current_num += 1;
                    current_streak += 1;
                }

                // 5. Update the longest streak found so far
                longest_streak = std::max(longest_streak, current_streak);
            }
        }

        return longest_streak;

    }
};
