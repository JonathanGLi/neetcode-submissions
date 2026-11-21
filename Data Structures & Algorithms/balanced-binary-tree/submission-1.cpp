/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:


    bool balanced = true;

    int recurse(TreeNode* root) {

        if (root == nullptr) {
            return 0;
        }

        int left_height = recurse(root->left);
        int right_height = recurse(root->right);

        if ((left_height - right_height > 1) || (right_height - left_height > 1)) {
            balanced = false;
        }

        return max(left_height, right_height) + 1;

    }


    bool isBalanced(TreeNode* root) {
        recurse(root);
        return balanced;
    }
};
