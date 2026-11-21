class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        



        unordered_map<string, vector<string>> map;

        for (string& s : strs) {
            vector<int> letters(26, 0);

            for (char c : s) {
                letters[c - 'a'] ++;
            }

            string letterCountEncoding = "";

            for (int i = 0; i < 26 ; i++){
                letterCountEncoding += "#";
                letterCountEncoding += to_string(letters[i]);
            }


            map[letterCountEncoding].push_back(s);


        }


        vector<vector<string>> res;

        for (auto& pair : map){
            res.push_back(pair.second);
        }

        return res;

    }
};
