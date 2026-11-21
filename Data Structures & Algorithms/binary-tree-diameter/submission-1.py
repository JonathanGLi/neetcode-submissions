# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0
        
        def dfs_diameter(root):

            nonlocal res

            if root is None:
                return 0
            else:

                a = dfs_diameter(root.left)
                b = dfs_diameter(root.right)

                res = max(a+b, res)

                return max(a, b)+1

        x  = dfs_diameter(root)

        return res
                