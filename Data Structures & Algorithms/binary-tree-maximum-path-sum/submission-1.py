# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxPathSum = float('-inf')#40

        def dfs(node):

            nonlocal maxPathSum

            #BC
            if not node:
                return 0

            # max sum path including node
            #resrsively call both children
            leftLine = dfs(node.left)
            rightLine = dfs(node.right)
            pSum = leftLine +rightLine + node.val
            print(pSum)

            maxPathSum = max(maxPathSum, pSum)

            res = max(0, max(leftLine + node.val, rightLine + node.val))

            #sum of the largest linkedlist starting at node
            return res

        dfs(root)

        return maxPathSum