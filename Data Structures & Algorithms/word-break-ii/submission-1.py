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
        def dfs(i):

            if i == n:
                return [""]

            if i in memo:
                return memo[i]

            print("h2i")
            memo[i] = []
            cur = root
            word = ""
            j = i
            while j < len(s) and s[j] in cur.next:
                word += s[j]
                cur = cur.next[s[j]]
                j += 1
                if cur.isWord:
                    suffixes = dfs(j)
                    for suf in suffixes:
                        if suf == "":
                            memo[i].append(word)
                        else:
                            memo[i].append(word + ' ' + suf)


            return memo[i]

        print(memo)

        return dfs(0)





            # traverse when s[i] is a child in tire
            # if we get to a end of a word in trie, we split
            # if we reach the end, start appending the letters back up

            #when we are at the end of a word, we memoize the dfs calls based on index
            #dfs(i) returns  all the suffix splits we can get, 
            #reverse the sentences at the end






