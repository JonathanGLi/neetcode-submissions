class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        vector<int> preprod(nums.size(), 1);
        vector<int> postprod(nums.size(), 1);

        //preprod and post prod arrays
        for (int i = 1; i < nums.size(); i++) {
            preprod[i] = preprod[i-1] * nums[i-1];

            int j = nums.size() - i - 1;
            postprod[j] = postprod[j+1] * nums[j+1];
            std :: cout << j << "j ";
            std :: cout << nums[j+1] << " ";
            std :: cout << preprod[i] << " ";
            std :: cout << postprod[j] << " ";
        }
        // 1, 1, 2, 8
        // 48, 24, 6, 1

        vector<int> res(nums.size(), 1);
        // loop through res array
        for (int i = 0; i < nums.size(); i++) {
            res[i] = preprod[i] * postprod[i];

        }

        return res;

    }
};
