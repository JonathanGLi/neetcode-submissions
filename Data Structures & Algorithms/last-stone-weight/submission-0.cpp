class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        
        priority_queue<int> maxHeap;

        //add stones to heap
        for (int stone : stones) {
            maxHeap.push(stone);
        }


        //continue to smash stones
        while (maxHeap.size() > 1) {
            int stone_1 = maxHeap.top();
            maxHeap.pop();
            int stone_2 = maxHeap.top();
            maxHeap.pop();

            if (stone_1 == stone_2) {
                continue;
            }
            else if (stone_1 > stone_2) {
                int newStone = stone_1 - stone_2;
                maxHeap.push(newStone);
            }

        }

        if (maxHeap.size() == 1) {
            return maxHeap.top();
        }
        else {
            return 0;
        }

    }
};
