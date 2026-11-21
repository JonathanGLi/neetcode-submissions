class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        
        adj = {c: set() for w in words for c in w}


        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            l = min(len(w1), len(w2))

            if len(w2) < len(w1) and w1[:l] == w2[:l]:
                return ""

            for j in range(l):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        

        visited = {} # true = seen ever, false = seen this

        arr = []

        def dfs(c):

            if c in visited:
                return visited[c]

            visited[c] = False

            for n in adj[c]:
                if dfs(n) == False:
                    return False

            visited[c] = True
            arr.append(c)

        for c in adj:
            if dfs(c) == False:
                return ""

        arr.reverse()

        return "".join(arr)


