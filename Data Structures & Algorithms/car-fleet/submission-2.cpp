class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        

        vector<tuple<int, double>> arry (position.size());

        for (int i = 0; i < position.size(); i++) {
            double eta = static_cast<double>(target - position[i]) / speed[i];
            arry[i] = make_tuple(position[i], eta);
        }    

        sort(arry.begin(), arry.end());

        for (auto& p : arry) {
            cout << get<0>(p)<< "_"<< get<1>(p)<< endl;
        }

        int res = 0;
        double curEta = 0;
        for (int i = arry.size()-1; i >=0; i--) {
            if (curEta < get<1>(arry[i])) {
                res++;
                curEta = max(curEta, get<1>(arry[i]));
            }
        }
        return res;
        // vector<tuple(int, double)> stack;
        // for (auto& pair : arry) {
        //     if (!stack.empty() && get<1>(stack.back()))
        // }
    }
};
