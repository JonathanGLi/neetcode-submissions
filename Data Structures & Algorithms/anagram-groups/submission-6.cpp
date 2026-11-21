class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> map;

        for (string& s : strs) {
            vector<int> letters(26, 0);
            for (char c : s) {
                letters[c - 'a'] ++;
            }


            string ss = to_string(letters[0]);

            for (int i = 1; i < letters.size(); i++) {
                ss += ",";
                ss += to_string(letters[i]);
            }
            map[ss].push_back(s);
        }


        vector<vector<string>> result;
        for (auto& pair : map) {
            result.push_back(pair.second);

        } 
        return result;

    }
};
