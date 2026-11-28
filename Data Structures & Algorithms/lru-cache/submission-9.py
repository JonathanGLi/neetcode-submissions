class DoublyLinkedList:
    def __init__(self, key = 0, val = 0):

        self.key = key
        self.val = val

        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):

        self.cap = capacity

        # Initialize DoublyLinkedList. 
        self.start = DoublyLinkedList()
        self.end = DoublyLinkedList()
        self.start.right = self.end
        self.end.left = self.start

        self.mapp = {}

        self.size = 0
        

    def get(self, key: int) -> int:

        if key in self.mapp:

            #move it to front
            node = self.mapp[key]
            self.remove(node)
            self.insert(node)

            return node.val

        else:
            return -1

        

    def put(self, key: int, value: int) -> None:

        if key in self.mapp:
            self.remove(self.mapp[key])
            self.size -= 1

        node = DoublyLinkedList(key, value)

        self.mapp[key] = node
        self.insert( node)
        self.size += 1

        if self.size > self.cap:
            print('key, val', key, value)
            print(self.end.left.val)
            node = self.end.left
            self.mapp.pop(node.key)
            self.remove(node)
            print(self.end.left.val)
            self.size = self.cap
        
    def insert(self, node) -> None:
        right_node = self.start.right
        
        self.start.right = node
        node.left = self.start

        node.right = right_node
        right_node.left = node

    def remove(self, node) -> None:
        node.left.right, node.right.left = node.right, node.left


