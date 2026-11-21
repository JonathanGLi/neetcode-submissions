class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        int l = nums.size();
        vector<int> prefixProducts(l);
        vector<int> suffixProducts(l);

        prefixProducts[0] = 1;
        suffixProducts[l-1] = 1;

        for (int i = 1; i < l; i++) {
            int j = l - i - 1;

            prefixProducts[i] = prefixProducts[i-1] * nums[i-1];
            suffixProducts[j] = suffixProducts[j+1] * nums[j+1];

        }


        vector<int> res(l);
        for (int i = 0; i < l; i++) {
            res[i] = prefixProducts[i] * suffixProducts[i];
        }

        return res;
    }
};
