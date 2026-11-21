# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        p_idx = i_ind = 0

        def dfs(limit):
            nonlocal p_idx, i_ind

            if p_idx == len(preorder):
                return None

            if inorder[i_ind] == limit:
                i_ind+=1
                return None

            node = TreeNode(preorder[p_idx])
            p_idx+=1
            node.left = dfs(node.val)
            node.right = dfs(limit)

            return node

        return dfs(float("inf"))





