# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(preorder_arr, inorder_arr):

            if not preorder_arr or not inorder_arr:
                return None

            node = TreeNode(preorder_arr[0])
            mid = inorder_arr.index(preorder_arr[0])
            node.left = build(preorder_arr[1:mid+1], inorder_arr[0:mid])
            node.right = build(preorder_arr[mid+1:], inorder_arr[mid+1:])
            return node
            
        return build(preorder, inorder)

        #first in poreorder is root
        #split inorder by root

        #