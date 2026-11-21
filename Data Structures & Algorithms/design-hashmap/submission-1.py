class Node:

    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next 


class MyHashMap:

    def __init__(self):
        self.map = [Node() for i in range (10000)]
        self.size = 10000
        

    def put(self, key: int, value: int) -> None:
        node = self.map[key%self.size]

        while node.next != None:
            node = node.next
            if node.key == key:
                node.val = value
                return 

        node.next = Node(key, value)

        print(key, value)
        print(self.map[key%self.size].next.key, self.map[key%self.size].next.val)

        

    def get(self, key: int) -> int:
        node = self.map[key % self.size]
        while node.key != key:
            node = node.next
            if not node:
                return -1

        return node.val

    def remove(self, key: int) -> None:
        node = self.map[key%self.size]
        if node.next == None:
            return 

        while node.next.key != key:
            node = node.next
            if node.next == None:
                return 

        node.next = node.next.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)