class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        unordered_map<int, tuple<int, int>> map;
        int maxx = 0;

        unordered_set<int> s(nums.begin(), nums.end());

        for (int num : s) {

            if (map.find(num+1) != map.end() && map.find(num-1) != map.end()) {
                int a1 = get<0>(map[num-1]);
                int b1 = get<1>(map[num-1]);
                int a2 = get<0>(map[num+1]);
                int b2 = get<1>(map[num+1]);
                map.erase(num-1);
                map.erase(num+1);
                map[a1] = make_tuple(a1, b2);
                map[b2] = make_tuple(a1, b2);

                if ((b2 - a1 + 1)> maxx) {
                    maxx = b2 - a1 + 1;
                }
            }
            else if (map.find(num+1) != map.end()) {

                int a = get<0>(map[num+1]);
                int b = get<1>(map[num+1]);
                map.erase(num+1);
                map[num] = make_tuple(num, b);
                map[b] = make_tuple(num, b);

                if ((b - num + 1)> maxx) {
                    maxx = b - num + 1;
                }
            }
            else if (map.find(num-1) != map.end()) {
                int a = get<0>(map[num-1]);
                int b = get<1>(map[num-1]);
                map.erase(num-1);
                map[num] = make_tuple(a, num);
                map[a] = make_tuple(a, num);

                if ((num - a + 1)> maxx) {
                    maxx = num - a + 1;
                }
            }
            else {
                map[num] = make_tuple(num, num);
                if (1 > maxx) {
                    maxx = 1;
                }
            } 

        }

        return maxx;
    }
};
