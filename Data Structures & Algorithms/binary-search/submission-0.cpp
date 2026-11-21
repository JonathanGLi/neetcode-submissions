class Solution {

    int binarySearch(vector<int>& nums, int l, int r, int target){

        cout << l << "_" << r << endl;
        int m = (l + r) / 2;


        if (nums[m] == target) {
            return m;
        }
        else if (l == r){
            return -1;
        }
        else if(nums[m] < target){
            return binarySearch(nums, m+1, r, target);
        }
        else if(nums[m] > target){
            return binarySearch(nums, l, m, target);
        }

    }
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, 0, nums.size()-1, target);
    }
};
