

class ListNode:
    def __init__(self, key: int, val: int, n: 'ListNode', p: 'ListNode'):
        self.key = key
        self.val = val
        self.next = n
        self.prev = p

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.start = ListNode(0, 0, None, None)
        self.end = self.start
        

    def get(self, key: int) -> int:
        if key in self.cache:

            if self.cache[key] != self.end:
                prev = self.cache[key].prev
                nxt = self.cache[key].next

                self.end.next = self.cache[key]
                self.cache[key].prev = self.end
                self.cache[key].next = None

                prev.next = nxt
                nxt.prev = prev

                self.end = self.end.next

            return self.cache[key].val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache[key].val = value

            if self.cache[key] != self.end:
                prev = self.cache[key].prev
                nxt = self.cache[key].next

                self.end.next = self.cache[key]
                self.cache[key].prev = self.end
                self.cache[key].next = None

                prev.next = nxt
                nxt.prev = prev

                self.end = self.end.next
        else:
            self.cache[key] = ListNode(key, value, None, None)

            self.end.next = self.cache[key]
            self.cache[key].prev = self.end
            self.cache[key].next = None

            self.end = self.end.next

        if len(self.cache) > self.cap:
            self.start = self.start.next
            del self.cache[self.start.key]
        
