class Solution {
public:
    bool isValid(string s) {
        

        vector<char> stack;

        for (char c : s) {
            if (!stack.empty()){
                char top = stack.back();
                if ((c == ')' && top == '(')
                ||(c == ']' && top == '[')
                ||(c == '}' && top == '{')) {
                    stack.pop_back();
                }
                else {
                    stack.push_back(c);
                }
            }
            else {
                stack.push_back(c);
            }
        }

        return stack.empty();
    }
};
