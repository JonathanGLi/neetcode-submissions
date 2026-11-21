class Solution {
public:

    string encode(vector<string>& strs) {

        string res = "";
        for (string s : strs) {
            int len = s.length();
            res += to_string(len) + "#" + s;
        }

        cout << res;
        return res;
    }

    vector<string> decode(string s) {
        
        int i = 0;
        int j = 0;
        vector<string> res;
        while (i < s.length()) {
            j=i;
            while (s[j] != '#') {
                j++;
            }
            int len = stoi(s.substr(i, j-i));

            i = j+1;
            j = i + len;

            string string_val = s.substr(i, j-i);
            res.push_back(string_val);
            i = j;
        }

        return res;
    }
};
