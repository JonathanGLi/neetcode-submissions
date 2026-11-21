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

        def dfs(node):
            
            nonlocal res
            if not node:
                res += "-#-"
                return

            res += "-" + str(node.val) + "-"

            dfs(node.left)


            dfs(node.right)

        dfs(root)

        print(res)
        return res



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        i = 0

        def getNext():
            nonlocal i
            a = i+1
            b = i+1
            while data[b] != "-":
                b += 1

            i = b+1

            return data[a:b]


        if data == "-#-":
            return None

        x = getNext()

        root = TreeNode(val = int(x))

        n = len(data)



        def dfs(node):

            nonlocal i

                


            print(i)

            if i == n:
                return


            x = getNext()
            if x != "#":
                left = TreeNode(val=int(x))
                node.left = left

                dfs(left)

            x = getNext()
            if x != "#":
                right = TreeNode(val=int(x))
                node.right = right

                dfs(right)

        dfs(root)

        return root











