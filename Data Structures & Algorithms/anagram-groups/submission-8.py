class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # Create lists of 24 letters long
        #We loop through the strings, and we create a 24-letter-long list. We map those lists in a dictionary to a list of the words that are anagrams of that list. 
        #Then we just append all of the values of that dictionary together to get our output. 

        letter_to_anagram_groups = defaultdict(list)
        
        for word in strs:

            letters = [0] * 26

            for c in word:
                letters[ord(c) - ord('a')] +=1

            letter_to_anagram_groups[tuple(letters)].append(word)

        return [group for group in letter_to_anagram_groups.values()]

            
