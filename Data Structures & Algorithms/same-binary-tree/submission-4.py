# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #time n1 + n2
        #space h1+h2

        res = [True]

        def dfs(node1, node2):


            if not node1 and not node2:
                return
            elif not node1:
                res[0] = False
                return
            elif not node2:
                res[0] = False
                return
            elif node1.val != node2.val:
                res[0] = False
                return

            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)

            

            return




        dfs(p, q)

        return res[0]
            
