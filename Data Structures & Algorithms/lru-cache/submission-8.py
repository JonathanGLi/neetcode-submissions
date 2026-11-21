class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self. right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}

        self.start = Node(-1, -1)
        self.end = Node(-1, -1)
        self.start.right = self.end
        self.end.left = self.start

    def remove(self, node):
        node.left.right, node.right.left = node.right, node.left

    def push(self, node):
        l = self.end.left
        r = self.end

        node.left = l
        node.right = r
        l.right = node
        r.left = node

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.remove(node)
            self.push(node)

            return node.val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:

        if key in self.mp:
            self.mp[key].val = value
            self.remove(self.mp[key])
            self.push(self.mp[key])
        else:

            node = Node(key, value)
            self.mp[key] = node

            self.push(node)

            if len(self.mp) > self.cap:
                rem_node = self.start.right
                del self.mp[rem_node.key]
                self.remove(rem_node)


        
