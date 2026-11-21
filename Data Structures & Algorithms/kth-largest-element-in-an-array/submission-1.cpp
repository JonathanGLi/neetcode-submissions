class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
        //minheap
        vector<int> heap (nums.begin(), nums.begin()+k);
        make_heap(heap.begin(), heap.end(), greater<int>());

        for (int i = k; i < nums.size(); i++) {
            if (nums[i] > heap[0]) {
                pop_heap(heap.begin(), heap.end(), greater<int>());
                heap.pop_back();
                heap.push_back(nums[i]);
                push_heap(heap.begin(), heap.end(), greater<int>());
            }
        }

        return heap[0];



    }
};
