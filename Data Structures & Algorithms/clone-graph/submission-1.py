"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        visited = {}
        
        def dfs(node):
            print("1")

            if not node:
                return None

            if node in visited:
                return visited[node]

            print("node.val", node.val)


            new_node = Node()
            new_node.val = node.val

            visited[node] = new_node

            for n in node.neighbors:
                print("nnn")
                new_neighbor = dfs(n)
                if new_neighbor:
                    new_node.neighbors.append(new_neighbor)
                    print("hi")


            return new_node

        return dfs(node)
            
