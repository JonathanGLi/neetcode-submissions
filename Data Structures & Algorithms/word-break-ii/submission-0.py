class TrieNode:
    def __init__(self):
        self.isWord = False
        self.next = {}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        n = len(s)

        #create trie

        root = TrieNode()
        for w in wordDict:
            cur = root
            for c in w:
                if c not in cur.next:
                    cur.next[c] = TrieNode()
                cur = cur.next[c]
            cur.isWord = True


        memo = {}

        #loop though s
        def dfs(i, cur):

            if i == n:
                if cur.isWord:
                    return [""]
                else:
                    return []

            if (i, cur) in memo:
                return memo[(i, cur)]

            memo[(i, cur)] = []
            if s[i] in cur.next:
                for w in dfs(i+1, cur.next[s[i]]):
                    memo[(i, cur)].append(w + s[i])

            if cur.isWord:
                for w in dfs(i, root):
                    memo[(i, cur)].append(w + ' ')

            return memo[(i, cur)]

        sentences = [sen[::-1] for sen in dfs(0, root)]

        return sentences





            # traverse when s[i] is a child in tire
            # if we get to a end of a word in trie, we split
            # if we reach the end, start appending the letters back up

            #when we are at the end of a word, we memoize the dfs calls based on index
            #dfs(i) returns  all the suffix splits we can get, 
            #reverse the sentences at the end






