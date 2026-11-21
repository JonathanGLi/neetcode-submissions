class Node:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:


    def __init__(self, capacity: int):

        self.capacity = capacity
        self.m = {}
        self.right = Node(0, 0)
        self.left = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev, next = self.right.prev, self.right
        node.prev = prev
        node.next = next
        prev.next = next.prev = node


    def get(self, key: int) -> int:

        if key in self.m:
            self.remove(self.m[key])
            self.insert(self.m[key])
            return self.m[key].val
        return -1


    def put(self, key: int, value: int) -> None:

        if key in self.m:
            self.remove(self.m[key])
            self.insert(self.m[key])
            self.m[key].val = value
        else:
            self.m[key] = Node(key, value)
            self.insert(self.m[key])

        if len(self.m) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.m[lru.key]




        
