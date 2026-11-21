class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        listt = self.m[key]

        l = 0
        r = len(listt) - 1

        while(l <= r):

            m = ((l + r)//2)

            if (
                ((listt[m][0] <= timestamp) and (m+1 == len(listt))) or
                ((listt[m][0] <= timestamp) and (listt[m+1][0] > timestamp))
                ):
                return listt[m][1]

            elif (
                ((listt[m][0] <= timestamp) and (listt[m+1][0] <= timestamp))):
                l = m + 1
            else:
                r = m - 1

        return ""
        
