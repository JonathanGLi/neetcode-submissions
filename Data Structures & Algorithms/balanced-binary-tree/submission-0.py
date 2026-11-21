# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        bal = True

        def dfs(node):
        
            nonlocal bal
            
            #null
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            #leaf
            if (left_height - right_height > 1 
            or right_height - left_height > 1):
                print("hi")
                bal = False
            return max(left_height, right_height) + 1

        dfs(root)

        return bal
            


        

        
