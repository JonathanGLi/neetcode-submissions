class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        D = defaultdict(list)
        
        #loop through strings
        for string in strs:

            #create array of letter counts
            arr = 26*[0]
            
            for c in string:
                arr[ord(c) - ord("a")] += 1

            # turn array in to tuple
            tup = tuple(arr)

            #put into dictionary and add word of value list

            D[tup].append(string)


        
        #return dictionary as list
        return D.values()

            
