class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> s;

        for (int i; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (s.count(complement)){
                return {s[complement], i} ;
            }
            s[nums[i]] = i;
        }

        return {};
    }
};
