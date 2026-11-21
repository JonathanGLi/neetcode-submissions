
class Node:

    def __init__(self):
        self.m = [None for i in range(26)]
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        self.root.m = [None for i in range(26)]
        

    def insert(self, word: str) -> None:
        i = 0
        node = self.root
        while i < len(word) and node.m[ord(word[i]) - ord('a')]:
            node = node.m[ord(word[i]) - ord('a')]
            i+=1
        while i < len(word):
            node.m[ord(word[i]) - ord('a')] = Node()
            node = node.m[ord(word[i]) - ord('a')]
            i+=1
        node.end = True


    def search(self, word: str) -> bool:
        i = 0
        node = self.root
        while i < len(word) and node.m[ord(word[i]) - ord('a')]:
            node = node.m[ord(word[i]) - ord('a')]
            i+=1
        return i == len(word) and node.end == True

    def startsWith(self, prefix: str) -> bool:
        word = prefix
        i = 0
        node = self.root
        while i < len(word) and node.m[ord(word[i]) - ord('a')]:
            node = node.m[ord(word[i]) - ord('a')]
            i+=1
        return i == len(word)
        