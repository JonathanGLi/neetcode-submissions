class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        D = defaultdict(list)

        for s in strs:

            count = 26 * [0]

            for c in s:
                count[ord(c) - ord("a")]+=1

            D[tuple(count)].append(s)

        return D.values()



