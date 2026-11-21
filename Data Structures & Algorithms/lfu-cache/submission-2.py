class Listnode:
    def __init__(self, t = 0, val = -1, key = -1):
        self.key = key
        self.val = val
        self.freq = 1
        self.t = t
        self.prev = None
        self.next = None



class LFUCache:

    def __init__(self, capacity: int):

        #maps freq to list of nodes
        self.freqMap = {}

        #maps keys to their nodes
        self.map = {}

        self.cap = capacity
        self.count = 0
        self.minFreq = 0

    def initList(self, freq):
        self.freqMap[freq] = [Listnode(1), Listnode(2)]
        self.freqMap[freq][0].next = self.freqMap[freq][1]
        self.freqMap[freq][1].prev = self.freqMap[freq][0]

    def removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

        freq = node.freq
        #if empty
        if self.freqMap[freq][0].next == self.freqMap[freq][1]:
            #if sel
            if self.minFreq == freq:
                self.minFreq += 1

    def addNode(self, node):
        freq = node.freq

        prev = None
        next = None
        if freq not in self.freqMap:
            self.initList(freq)
            prev = self.freqMap[freq][0]
            next = self.freqMap[freq][1]
        else:
            prev = self.freqMap[freq][1].prev
            next = self.freqMap[freq][1]

        prev.next, node.prev = node, prev
        node.next, next.prev = next, node


    def get(self, key: int) -> int:

        if key not in self.map:
            return -1
        node = self.map[key]
        # remove node from its linked list
        self.removeNode(node)

        node.freq += 1

        self.addNode(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.map:
            self.map[key].val = value
            self.removeNode(self.map[key])
            self.map[key].freq += 1
            self.addNode(self.map[key])
        else:
            #makes node
            self.map[key] = Listnode(val = value, key = key)

            #cap
            if self.count == self.cap:
                node = self.freqMap[self.minFreq][0].next
                self.removeNode(node)
                k = node.key
                self.map.pop(k)
                self.count -= 1 

            #add new node
            # freq set
            self.minFreq = 1
            self.addNode(self.map[key])  
            self.count += 1 


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)