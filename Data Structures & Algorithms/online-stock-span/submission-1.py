class StockSpanner:

    def __init__(self):
        self.stack = []
        self.count = 0
        

    def next(self, price: int) -> int:
        self.count += 1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        
        start = 0
        if self.stack:
            start = self.stack[-1][1]
        dist = self.count - start

        self.stack.append((price, self.count))

        return dist
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)