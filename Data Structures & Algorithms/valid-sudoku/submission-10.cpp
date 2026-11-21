class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        


        for (int i = 0; i< 9; i++) {
            unordered_set<int> s1;
            for (int j = 0; j< 9; j++) {
                
                if (board[i][j] != '.' && s1.count(board[i][j])) {
                    return false;
                }
                s1.insert(board[i][j]);
            }
        }

        for (int j = 0; j< 9; j++) {
            unordered_set<int> s2;
            for (int i = 0; i< 9; i++) {
                
                if (board[i][j] != '.' && s2.count(board[i][j])) {
                    return false;
                }
                s2.insert(board[i][j]);
            }
        }
        for (int j = 0; j< 3; j++) {
            for (int i = 0; i< 3; i++) {
                unordered_set<int> s3;
                for (int j1 = 0; j1< 3; j1++) {
                    for (int i1 = 0; i1< 3; i1++) {
                        if (board[i*3 + i1][j*3+j1] != '.' && s3.count(board[i*3 + i1][j*3+j1])) {
                            return false;
                        }
                        s3.insert(board[i*3 + i1][j*3+j1]);
                    }
                }
            }
        }

        return true;

    }
};
