class FreqStack:

    def __init__(self):

        # freq => vals with that freq
        self.freq_to_vals = defaultdict(list)

        #max freq
        self.max_freq = 0

        #val => feq
        self.val_to_freq = defaultdict(int)
        

    def push(self, val: int) -> None:
        print("push")
        self.val_to_freq[val] += 1
        self.freq_to_vals[self.val_to_freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.val_to_freq[val])
        print(self.freq_to_vals)


    def pop(self) -> int:
        print("pop")
        res = self.freq_to_vals[self.max_freq].pop()
        self.val_to_freq[res] -= 1
        if len(self.freq_to_vals[self.max_freq]) == 0:
            self.max_freq -=1

        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()