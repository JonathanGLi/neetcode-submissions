class Solution {
public:

    string encode(vector<string>& strs) {
        

        //(string length)#string

        string res = "";

        for (string& s : strs) {
            int len = s.length();
            res += to_string(len);
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
            //i = j
            while (s[j] != '#') {
                j ++;
            }

            int len = stoi(s.substr(i, j-i));

            //get the word
            i = j + 1;
            j = i + len;

            string word = s.substr(i, j-i);

            //
            res.push_back(word);

            i = j;

        }

        return res;
    }
};
