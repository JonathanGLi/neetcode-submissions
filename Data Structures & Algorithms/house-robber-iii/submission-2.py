# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        #maps each node.val to max money you can get from that node
        memo = {}

        def dfs(node):

            if not node:
                return 0

            if (node) in memo:
                return memo[node]


            #take
            a = node.val
            if node.left and node.left.left:
                a += dfs(node.left.left)
            if node.left and node.left.right:
                a += dfs(node.left.right)
            if node.right and node.right.right:
                a += dfs(node.right.right)
            if node.right and node.right.left:
                a += dfs(node.right.left)

            # skip 
            b = 0
            if node.left:
                b += dfs(node.left)
            if node.right:
                b += dfs(node.right)

            res = max(a, b)

            memo[node] = res 


            return res

        return dfs(root)
        




