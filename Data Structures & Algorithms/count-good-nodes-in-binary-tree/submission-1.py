# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0
        
        def dfs(node, n):

            nonlocal count

            if not node:
                return

            new_n = max(n, node.val)

            dfs(node.left, new_n)
            dfs(node.right, new_n)
            
            if node.val >= n:
                count += 1

            return 

        dfs(root, float('-inf'))

        return count


