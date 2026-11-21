class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1] * k 

        self.k = k
        self.count = 0
        self.start = 0
        self.end = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        else:
            self.arr [self.end] = value
            self.end = (self.end + 1) % self.k
            self.count += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.arr [self.start] = -1
            self.start = (self.start + 1) % self.k
            self.count -= 1
            return True  

    def Front(self) -> int:
        return self.arr[self.start]

    def Rear(self) -> int:
        return self.arr[self.end-1]   

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.count == self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()