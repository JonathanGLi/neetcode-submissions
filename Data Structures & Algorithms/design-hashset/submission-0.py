class List:
    def __init__(self, key = None):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.s = [List() for i in range(self.size)]
        

    def add(self, key: int) -> None:
        if self.contains(key) == False:
            cur = self.s[key%self.size]
            node = List(key)
            node.next = cur.next
            cur.next = node


    def remove(self, key: int) -> None:
        prev = self.s[key%self.size]
        cur = prev.next
        while(cur!= None):
            if cur.key == key:
                prev.next = cur.next
                return 

            prev = cur
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.s[key%self.size]
        while(cur!= None):
            if cur.key == key:
                return True

            cur = cur.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)