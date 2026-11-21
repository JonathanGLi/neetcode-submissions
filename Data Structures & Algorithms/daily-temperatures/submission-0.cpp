class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        


        vector<int> res (temperatures.size(), 0);
        vector<tuple<int, int>> stack;
        stack.push_back(make_tuple(temperatures[0], 0));

        for (int i = 1; i < temperatures.size(); i++) {

            while (!stack.empty() && temperatures[i] > get<0>(stack.back())) {
                int diff =  i - get<1>(stack.back());
                int idx = get<1>(stack.back());
                res[idx] = diff;
                stack.pop_back();

            }
            stack.push_back(make_tuple(temperatures[i], i));

        }

        return res;
    }
};
