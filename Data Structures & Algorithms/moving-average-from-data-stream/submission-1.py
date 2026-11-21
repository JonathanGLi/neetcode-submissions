class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.size = size
        self.count = 0
        self.total = 0
        

    def next(self, val: int) -> float:
        self.q.append(val)
        self.count += 1

        rem = self.q.popleft() if self.count > self.size else 0

        self.total = self.total - rem + val

        return self.total / min(self.size, self.count)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
