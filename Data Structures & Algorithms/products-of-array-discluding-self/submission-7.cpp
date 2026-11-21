class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        //fill pre and post
        vector<int> pre(nums.size(), 1);
        vector<int> post(nums.size(), 1);

        for (int i = 1; i < nums.size(); i++) {
            pre[i] = pre[i-1] * nums[i-1];

            int j = nums.size() - i - 1;

            post[j] = post[j+1] * nums[j+1];
        }

        //pre: 1, 1, 2, 8
        //post: 48, 24, 6, 1


        // fill res

        vector<int> res(nums.size(), 1);

        for (int i = 0; i < nums.size(); i++) {
            res[i] = pre[i] * post[i];
        }

        return res;
    }
};
