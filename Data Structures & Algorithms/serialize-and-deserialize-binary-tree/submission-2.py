# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        queue = deque([root])
        res = []
        print("hi")
        #loop through layer
        while(queue):

            node = queue.popleft()
        #add values of the layer
            if not node:
                res.append("N")
            # only add the layer if it has one node
            #add children of nodes to queue
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        res2 = ",".join(res)
        print(res2)
        return res2

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        d = data.split(',')
        print(d)

        if d[0] == "N":
            return None
        root = TreeNode(int(d[0]))
        #queue of nodes
        queue = deque([root])
        #index
        i = 1

        #loop through layer
        while queue:

            node = queue.popleft()

            #the children of the node are the next two indicies

            #if null, then set child to null
            #if node then set node val and add children to queue
            if d[i] != "N":
                node.left = TreeNode(int(d[i]))
                queue.append(node.left)
            i += 1

            if d[i] != "N":
                node.right = TreeNode(int(d[i]))
                queue.append(node.right)
            i += 1

        return root
