class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

        # xyxxyzbzbbisl

        # x

        # x => 0
        # y => 0
        # b=>6


        # map letter to start of that string
        map = {}

        for i in range(len(s)):

            if s[i] in map:

                for k, v in map.items():
                    if v > map[s[i]]:
                        map[k] = map[s[i]]
                continue

            map[s[i]] = i
            

        sett = set()
        for k, v in map.items():
            sett.add(v)

        starting = list(sett)

        starting.sort()

        starting.append(len(s))

        idx = [(starting[i+1] - starting[i]) for i in range(len(starting)-1)]

        return idx

        





        # map.values would be indexes and we sort and take substrings