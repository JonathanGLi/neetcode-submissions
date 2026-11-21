class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> res;
        
        for (const auto& s : strs) {
            vector<int> letters(26, 0);
            for (char c : s) {
                letters[c - 'a']++;
            }

            string key = to_string(letters[0]);
            for (int i = 1; i < letters.size(); i++){
                key += ',' + to_string(letters[i]);
            }
            res[key].push_back(s);


        }
        vector<vector<string>> result;
        for (const auto& pair : res) {
            result.push_back(pair.second);
        }

        return result;
    }
};
