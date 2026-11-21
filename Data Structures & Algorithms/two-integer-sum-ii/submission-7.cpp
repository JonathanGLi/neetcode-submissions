class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        

        int l = 0;
        int r  = numbers.size()-1;

        while(l < r) {
            int summ = numbers[l] + numbers[r];

            if (summ > target) {
                r--;
            }
            else if (summ < target) {
                l++;
            }
            else if (summ == target) {
                return {l+1, r+1};
            }
        }
    }
};
