class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num)) {
                std::cout << "seen.count(num)" << seen.count(num);
                return true;

            }
            seen.insert(num);
        }

        return false;
    }
};
