class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        

        //map number to count
        unordered_map<int, int> map;

        for (int n : nums) {
            map[n] ++;
        }


        //map the count to the array of numbers with that count
        std :: map<int, vector<int>, greater<int>> map2;

        for (auto& pair : map){
            map2[pair.second].push_back(pair.first);
        }

        //sort by count decreasing
        vector<int> res;
        int k_count = 0;

        for (auto& pair : map2){
            while (pair.second.size() > 0 && k_count < k) {
                res.push_back(pair.second.back());
                pair.second.pop_back();
                k_count++;
            }
        }
        //return array of the numbers

        return res;
    }
};
