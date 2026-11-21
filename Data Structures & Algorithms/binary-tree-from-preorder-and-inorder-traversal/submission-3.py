# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder and not inorder:
            return None

        mid = preorder[0]
        node = TreeNode(mid)
        idx = inorder.index(mid)
        node.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        node.right = self.buildTree(preorder[idx + 1:], inorder[idx+1:])

        return node