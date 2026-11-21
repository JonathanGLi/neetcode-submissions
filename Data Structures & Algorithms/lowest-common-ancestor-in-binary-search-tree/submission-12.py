# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node):

            # explore down the tree
            #min and max of values
            minn = min(p.val, q.val)
            maxx = max(p.val, q.val)

            #if both min and max are smaller go left
            if (minn < node.val) and (maxx < node.val):
                return dfs(node.left)

            # if both larger go right
            elif (minn > node.val) and (maxx > node.val):
                return dfs(node.right)
            #explore until cur val is between min and max
            else:
                return node


        return dfs(root)