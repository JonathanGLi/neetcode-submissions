class Solution {
public:

    void backtrack(int open, int closed, int n, vector<char>& stack, vector<string>& res){

        if (open == closed && closed== n) {
            res.push_back(string(stack.begin(), stack.end()));
            return;
        }
        if (open < n) {
            stack.push_back('(');
            backtrack(open+1, closed, n, stack, res);
            stack.pop_back();
        }
        if (open > closed) {
            stack.push_back(')');
            backtrack(open, closed+1, n, stack, res);
            stack.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        
        vector<char> stack;
        vector<string> res;
        backtrack(0, 0, n, stack, res);
        return res;

    }

};

