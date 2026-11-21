class MinStack {
private:
    vector<int> stack;
    vector<int> mStack;
public:
    MinStack() {
        stack = vector<int>();
        mStack = vector<int>();
    }
    
    void push(int val) {
        stack.push_back(val);
        if (mStack.size() == 0 || val <= mStack.back()) {
            mStack.push_back(val);
        }
    }
    
    void pop() {
        if (mStack.size() > 0) {
            if (mStack.size() > 0 && stack.back() == mStack.back()) {
                mStack.pop_back();
            } 
            stack.pop_back();
        }
    }
    
    int top() {
        if (stack.size() > 0) {
            return stack.back();
        }
    }
    
    int getMin() {
        if (mStack.size() > 0) {
            return mStack.back();
        }
    }
};
