class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        

        //map nums to their count

        unordered_map<int, int> map;

        for (int n : nums) {
            map[n] ++;
        }

        //map counts to a vector of numbers with that count in decreaasing sorted order
        std :: map<int, vector<int>, std :: greater<int>> map2;

        for (auto& pair : map) {
            map2[pair.second].push_back(pair.first);
        }

        //loop throught map2 and add k numbers to res

        vector<int> res;
        int k_count = k;

        for (auto& pair : map2) {
            while (k_count > 0 && pair.second.size() > 0) {
                res.push_back(pair.second.back());
                pair.second.pop_back();
                k_count--;

            }
        }

        return res;

    }
};
