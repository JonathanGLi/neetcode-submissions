class Solution {

struct Compare{
    bool operator() (const vector<int>& a, const vector<int>& b) {
        return a[0]* a[0]+a[1]*a[1] < b[0]*b[0]+b[1]*b[1];
    }
};

public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        
        //make maxheap with k points
        vector<vector<int>> heap(points.begin(), points.begin()+k);
        make_heap(heap.begin(), heap.end(), Compare());

        //loop through rest of points and update heap contain k smallest points
        for (int i = k; i < points.size(); i++) {
            int curDist = points[i][0]* points[i][0]+points[i][1]*points[i][1];
            int maxDist = heap[0][0]* heap[0][0]+heap[0][1]*heap[0][1];

            //if point is closer to the origin than the top of the heap
            if (curDist < maxDist) {
                //removal
                pop_heap(heap.begin(), heap.end(), Compare());
                heap.pop_back();
                //adding
                heap.push_back(points[i]);
                push_heap(heap.begin(), heap.end(), Compare());
            }
        }

        return heap;

    }
};
