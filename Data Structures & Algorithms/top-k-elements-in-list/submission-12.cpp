class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        //map elements to count
        unordered_map<int, int> elems_to_count;

        for (int num : nums) {
            elems_to_count[num]+=1;
        }

        //array mapping count to elems
        vector<vector<int>> count_to_elems(nums.size()+1);
        for (const auto& pair : elems_to_count) {
            count_to_elems[pair.second].push_back(pair.first);
        }

        vector<int> res;
        //append to res starting from the back until k = 0
        int i = count_to_elems.size()-1;
        int k_count = k;
        while (k_count > 0) {
            if (count_to_elems[i].size() > 0) {
                res.push_back(count_to_elems[i].back());
                count_to_elems[i].pop_back();
                k_count--;
            }
            else {
                i--;
            }
    
        }
        return res;
    }
};
