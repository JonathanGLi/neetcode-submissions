class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        int h = board.size();
        int w = board[0].size();
        
        for (int i = 0; i < h;i++) {
            unordered_set<char> s;
            for (int j = 0; j < w;j++) {
                if (s.count(board[i][j])) {
                    return false;
                }
                if (board[i][j]!= '.') {
                    s.insert(board[i][j]);
                }
                
            }
        }

        for (int j = 0; j < w;j++) {
            unordered_set<char> s;
            for (int i = 0; i < h;i++) {
                if (s.count(board[i][j])) {
                    return false;
                }
                if (board[i][j]!= '.') {
                    s.insert(board[i][j]);
                }
            }
        }

        for (int i1 = 0; i1 < 3;i1++) {
            for (int j1 = 0; j1 < 3; j1++) {
                unordered_set<char> s;
                for (int i = i1*3; i < (i1+1)*3; i++) {
                    for (int j = j1*3; j < (j1+1)*3; j++) {
                        
                        if (s.count(board[i][j])) {
                            return false;
                        }
                        if (board[i][j]!= '.') {
                            s.insert(board[i][j]);
                        }

                    }
                }
            }
        }

        return true;
    }
};
