# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #n, 1
        maxDepth = [0]

        def dfs(node, curDepth):

            if not node:
                return

            curDepth+= 1

            maxDepth[0] = max(maxDepth[0], curDepth)

            dfs(node.left, curDepth)
            dfs(node.right, curDepth)

            return 


        dfs(root, 0)

        return maxDepth[0]


            

            
