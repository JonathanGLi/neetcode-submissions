class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        

        vector<pair<int, double>> arry (position.size());

        for (int i = 0; i < position.size(); i++) {
            double eta = 1.0 * (target - position[i]) / ( (speed[i]));
            arry[i] = {position[i], eta};
        }    

        sort(arry.begin(), arry.end());

        for (auto& p : arry) {
            cout << p.first << "_"<< p.second << endl;
        }

        int res = 0;
        double curEta = 0;
        for (int i = arry.size()-1; i >=0; i--) {
            if (curEta < arry[i].second) {
                res++;
                curEta = max(curEta, arry[i].second);
            }
        }
        return res;
        // vector<tuple(int, double)> stack;
        // for (auto& pair : arry) {
        //     if (!stack.empty() && get<1>(stack.back()))
        // }
    }
};
