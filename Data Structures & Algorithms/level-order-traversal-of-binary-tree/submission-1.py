# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        D = defaultdict(list)

        def dfs(node, depth):

            if node is None:
                return 

            D[depth].append(node.val)

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

            return
            

        dfs(root, 0)

        res = D.values()
        return list(res)

            