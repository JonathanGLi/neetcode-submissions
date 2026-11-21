# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        

        #postorder traversal
        #dfs to leaves
        #dfs returns the new Tree
        # n time, height space for recursive calls

        def dfs(node):

            #if all children are deleted and node has target val
                #return None
            if node.left:
                node.left = dfs(node.left)
            if node.right:
                node.right = dfs(node.right)

            # if node is a child and val == Target
                #return None
            if not node.left and not node.right and node.val == target:
                return None

            #return Node
            return node



        return dfs(root)


