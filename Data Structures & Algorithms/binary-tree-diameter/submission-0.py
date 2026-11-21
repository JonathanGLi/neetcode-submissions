# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs_diameter(root):
            if root is None:
                return (0, 0)
            else:

                a, b = dfs_diameter(root.left)
                c, d = dfs_diameter(root.right)

                diameter = max(b, d)

                return (max(a, c)+1, max(a+c, diameter))

        x, y = dfs_diameter(root)

        return max(x-1, y)
                