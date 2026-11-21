# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs_same(root1, root2):
            print("hi")
            if not root1 and not root2:
                return True
            elif root1 and root2 and root1.val == root2.val:
                return dfs_same(root1.left, root2.left) and dfs_same(root1.right, root2.right)
            else:
                return False

        
        def dfs(root):

            if not subRoot:
                return True
            if subRoot and not root:
                return False
            elif root and subRoot and root.val == subRoot.val:
                return dfs_same(root, subRoot) or dfs(root.left) or dfs(root.right)
            else:
                return False or dfs(root.left) or dfs(root.right)

        return dfs(root)