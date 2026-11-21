class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
        vector<int> stack;

        for (string t : tokens) {
            if(t == "+") {
                int b = stack.back();
                stack.pop_back();
                int a = stack.back();
                stack.pop_back();

                stack.push_back(a+b);
            }
            else if(t == "-") {
                int b = stack.back();
                stack.pop_back();
                int a = stack.back();
                stack.pop_back();

                stack.push_back(a-b);
            }
            else if(t == "*") {
                int b = stack.back();
                stack.pop_back();
                int a = stack.back();
                stack.pop_back();

                stack.push_back(a*b);
            }
            else if(t == "/") {
                int b = stack.back();
                stack.pop_back();
                int a = stack.back();
                stack.pop_back();

                stack.push_back(a/b);
            }
            else {
                stack.push_back(stoi(t));
            }
        }

        return stack.back();
    }
};
