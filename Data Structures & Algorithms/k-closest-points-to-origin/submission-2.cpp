


class Solution {
public:

    struct Compare {
        bool operator() (vector<int>& a, vector<int>& b) {
            return a[0] * a[0] + a[1] * a[1] > b[0] * b[0] + b[1] * b[1];
        }
    };
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {

        
        priority_queue<vector<int>, vector<vector<int>>, decltype((Compare()))> minHeap((Compare()));

        for (const auto& point : points) {
            minHeap.push({point[0], point[1]});
        }

        vector<vector<int>> result;
        for (int i = 0; i < K; ++i) {
            result.push_back(minHeap.top());
            minHeap.pop();
        }
        return result;
    }
};