class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)
        
        #dictionary with 
        #tubles of lettercount as keys
        #list of words as values

        for s in strs:
            count = 26 * [0]

            for c in s:
                count[ord(c) - ord("a")] += 1

            map[tuple(count)].append(s)

        return map.values()
