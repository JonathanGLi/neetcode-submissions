# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        stack = [root]
        visit = [False]
        res = []

        while stack:
            s, v = stack.pop(), visit.pop()
            if v:
                res.append(s.val)
            elif s:
                stack.append(s)
                visit.append(True)
                stack.append(s.right)
                visit.append(False)
                stack.append(s.left)
                visit.append(False)

        return res
            



