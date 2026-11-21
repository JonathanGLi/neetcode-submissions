# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        pIdx, iIdx = 0, 0
        
        def dfs(limit):
            nonlocal pIdx, iIdx
            if pIdx == len(preorder):
                return None
            if inorder[iIdx] == limit:
                iIdx+=1
                return None

            node = TreeNode(preorder[pIdx])
            pIdx+=1
            node.left = dfs(node.val)
            node.right = dfs(limit)
            return node

        return dfs(float('inf'))
            