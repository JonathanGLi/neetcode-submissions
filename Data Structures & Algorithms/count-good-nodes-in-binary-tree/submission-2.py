# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        #n time, 1 space
        # keep track of largest seen

        counter = 0

        def dfs(node, largest):

            nonlocal counter

            if node == None:
                return
            
            if node.val >= largest:
                counter += 1
                new_largest = node.val
            else:
                new_largest = largest


            dfs(node.left, new_largest)
            dfs(node.right, new_largest)

        dfs(root, -float('inf'))

        return counter
