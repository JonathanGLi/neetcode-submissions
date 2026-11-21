# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        


        #dfs, look left child, node, right child
        #increment counter right beofre return
        # return curnode.val when counter == k

        count = [1]
        res = []

        def dfs(node):


            if not node:
                return 

            dfs(node.left)

            if count[0] == k:
                res.append(node.val)
                return
            count[0] += 1

            dfs(node.right)

            return 

        dfs(root)

        return res[0]

