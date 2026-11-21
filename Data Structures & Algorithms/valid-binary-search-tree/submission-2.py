# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        
        def dfs(node, minn, maxx):


            if node == None:
                return True

            if node.val <= minn or node.val >= maxx:
                return False

            
            leftRes = dfs(node.left, minn, node.val)
            rightRes =  dfs(node.right, node.val, maxx)

            return leftRes and rightRes





        
        return dfs(root, -float('inf'), float('inf'))
