class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int maxProf = 0;
        int buy = prices[0];

        for (int p : prices) {
            buy = min(buy, p);
            maxProf = max(maxProf, p - buy);
        }
        return maxProf;


    }
};
