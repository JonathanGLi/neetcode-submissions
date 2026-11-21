# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        res = None
        
        def dfs(node):

            nonlocal res

            if not node:
                print("case 1")
                return (False, False)

            a, b = dfs(node.left)
            c, d = dfs(node.right)

            print(a, b, c, d)
            print(node.val)
            if (a and b) or (c and d):
                print("case 2")
                return (True, True)
            elif (a or c or node.val == p.val) and (b or d or node.val == q.val)and res == None:
                print("case 3")
                res = node
                return (True, True)
            elif node.val == p.val:
                print("case 4")
                return (True, False)
            elif node.val == q.val:
                print("case 5")
                return (False, True)
            else:
                print("case 6")
                return (a or c , b or d)

        dfs(root)

        return res