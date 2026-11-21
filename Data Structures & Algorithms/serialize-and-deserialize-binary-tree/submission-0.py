# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = ""

        def dfs(node):#1, 2

            nonlocal res

            if not node:
                res = res + "#"
                res = res + "!"
                return

            res = res + "#"
            res = res + str(node.val)

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(res)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        i, j = 1, 1

        def dfs():

            nonlocal i, j

            if j >= len(data):
                return None

            while data[j] != "#":
                j+=1
                if j >= len(data):
                    return None
            val = data[i:j]

            j+=1
            i = j

            if val == "!":
                return None
            else:
                node = TreeNode(int(val))

                node.left = dfs()
                node.right = dfs()
                return node

        return dfs()





