# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        

        depths = set()
        #5:05

        # left count > right count

        # all leaves depth different by 1

        # return count going up
        # increase depth going down
        # dfs

        res = [True]

        def dfs(node, depth):

            if not node:
                depths.add(depth)
                return 0


            left_count, right_count = 0, 0
            left_count = dfs(node.left, depth+1)
            right_count = dfs(node.right, depth+1)

            # print(node.val, depth)
            # print("l, r", left_count, right_count)  

            if right_count > left_count:
                res[0] = False

            return left_count + right_count + 1


        dfs(root, 0)

        d = list(depths)

        # print(res[0])
        # print(len(depths) <= 2)
        if res[0] and len(depths) <= 2:

            if depths == 2 and abs(d[1] - d[0]) > 1:
                return False

        
            return True
        else:
            return False
        