class Solution {
public:

    string encode(vector<string>& strs) {

        string res = "";

        for (string& s : strs) {
            res += to_string(s.length());
            res += "#";
            res += s;
        }

        return res;
    }

    vector<string> decode(string s) {


        vector<string> res;
        int i = 0;
        int j = 0;

        while (i < s.length()) {

            while (s[j] != '#') {
                j++;
            }

            int len = stoi(s.substr(i, j-i));

            i = j + 1;


            string word = s.substr(i, len);
            j = i + len;
            res.push_back(word);

            i = j;

        }

        return res;
    }
};
