# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        Q = collections.deque()
        Q.append(root)

        while len(Q) > 0:
            level = []
            qlen = len(Q)

            for i in range(qlen):
                a = Q.popleft()
                if a:
                    level.append(a.val)
                    Q.append(a.left)
                    Q.append(a.right)

            if len(level) > 0:
                res.append(level)

        return res

            


            