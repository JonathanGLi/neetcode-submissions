# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # each path has a root
        # find each max path sum for each room starting from bottom


        def dfs(node):

            if node == None:
                return -float('inf'), -float('inf')


            left_maxPathSum, left_maxPathSumWithRoot = dfs(node.left)
            right_maxPathSum, right_maxPathSumWithRoot = dfs(node.right)

            maxSumWithNodeSingle = node.val
            maxSumWithNodeSingle = max(node.val + left_maxPathSumWithRoot, maxSumWithNodeSingle)
            maxSumWithNodeSingle = max(node.val + right_maxPathSumWithRoot, maxSumWithNodeSingle)
            maxSumWithNode = max(node.val + left_maxPathSumWithRoot + right_maxPathSumWithRoot, maxSumWithNodeSingle)


            maxPathSum = max(max(maxSumWithNode, left_maxPathSum), right_maxPathSum)
            maxPathSumWithRoot = maxSumWithNodeSingle

            return maxPathSum, maxPathSumWithRoot

        res, _ = dfs(root)

        return res


