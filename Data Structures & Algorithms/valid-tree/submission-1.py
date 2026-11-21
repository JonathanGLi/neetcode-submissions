class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        


        if n-1 != len(edges):
            return False
        # acyclic, 

        m = defaultdict(set)


        #n , n
        for e in edges:
            m[e[0]].add(e[1])
            m[e[1]].add(e[0])

        print(m)

        def isCycle(i, seen, parent):
            
            print(i, seen, parent)

            sett = m[i]

            if sett ==None:
                return False

            if i in seen:
                return True

            seen.add(i)

        
            for child in sett:
                if parent != child  and isCycle(child, seen, i):
                    return True


            return False
            
        
        for i in range(n):
            seen = set()
            if isCycle(i, seen, -1):
                return False

        return True


