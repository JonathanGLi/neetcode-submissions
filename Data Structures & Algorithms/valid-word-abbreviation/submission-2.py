class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        

        i, j = 0, 0

        while i < len(abbr) and j < len(word):
            if abbr[i].isdigit():
                k = i

                num = 0
                while k < len(abbr) and abbr[k].isdigit():
                    print(abbr[k])
                    if num == 0 and int(abbr[k]) == 0:
                        return False
                    num = 10 * num + int(abbr[k])
                    k+=1

                i = k
                j += num

            else:
                if abbr[i]!= word[j]:
                    return False
                i += 1
                j+=1


        return i == len(abbr) and j == len(word)

                