class Node:
    def __init__(self):

        self.isEnd = False
        self.arr = [None for i in range(26)]



class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        



        #tree
        #n*m, n*m

        #creates the tree
        root = Node()

        for word in words:

            cur = root
            for c in word:

                if not cur.arr[(ord(c) - ord('a'))]:
                    cur.arr[(ord(c) - ord('a'))] = Node()

                cur = cur.arr[(ord(c) - ord('a'))]

            cur.isEnd = True

        # def canForm(word):
        #     memo = defaultdict(bool)

        #     def rec(i, split):

        #         if (i, split) in memo:
        #             return memo[(i, split)]

        #         cur = root

        #         while i < len(word):

        #             c = word[i]
        #             if cur.arr[(ord(c) - ord('a'))]:
        #                 cur = cur.arr[(ord(c) - ord('a'))]

        #                 if cur.isEnd:
        #                     if rec(i+1, True):
        #                         return True

        #                 i+=1
        #             else:
        #                 memo[(i, split)] = False
        #                 return False

        #         res = cur.isEnd and split
        #         memo[(i, split)] = res
        #         return res

        #     return rec(0, False)


        def canForm(word):
            memo = {}

            def rec(i, split):

                if i == len(word):
                    return split  # Need at least 2 words

                if (i, split) in memo:
                    return memo[(i, split)]

                cur = root
                for j in range(i, len(word)):
                    idx = ord(word[j]) - ord('a')
                    if not cur.arr[idx]:
                        break
                    cur = cur.arr[idx]
                    
                    if cur.isEnd:
                        if j + 1 == len(word) and split == False:
                            break
                        if rec(j + 1, True):
                            memo[(i, split)] = True
                            return True

                memo[(i, split)] = False
                return False

            return rec(0, False)

        res = []

        for word in words:

            if canForm(word):

                res.append(word)

        return res


        # def canForm(word):
        #     memo = {}
            
        #     def rec(i, count):
        #         if i == len(word):
        #             return count >= 2  # Need at least 2 words
                
        #         if (i, count) in memo:
        #             return memo[(i, count)]
                
        #         cur = root
        #         for j in range(i, len(word)):
        #             idx = ord(word[j]) - ord('a')
        #             if not cur.arr[idx]:
        #                 break
        #             cur = cur.arr[idx]
                    
        #             if cur.isEnd:
        #                 if rec(j + 1, count + 1):
        #                     memo[(i, count)] = True
        #                     return True
                
        #         memo[(i, count)] = False
        #         return False
            
        #     return rec(0, 0)
