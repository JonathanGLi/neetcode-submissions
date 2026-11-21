# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        #right child first traversal
        maxHeight = -1
        #if height is creater, update height+=1 and then append to res list
        #n time, h space

        res = []

        def dfs(node, curHeight):

            nonlocal maxHeight

            if node == None:
                return


            if curHeight > maxHeight:
                maxHeight+=1
                res.append(node.val)

            dfs(node.right, curHeight+1)
            dfs(node.left, curHeight+1)

            return
            




        dfs(root, 0)

        return res
        