class CountSquares:

    # space n
    def __init__(self):

        #maps x coord to coordicates with that x
        self.mapXtoCoord = defaultdict(list)

        #coord => count
        self.coordCount = defaultdict(int)
        

    #1
    def add(self, point: List[int]) -> None:

        # mutable datatype

        #   cant      self.coordCount(point[0]) 
        coords = (point[0], point[1])
        self.coordCount[coords] += 1

        self.mapXtoCoord[coords[0]].append(coords)
        

    def count(self, point: List[int]) -> int:


        # #(n) loop


        count = 0
        x1 = point[0]
        y1 = point[1]

        for _, y2 in self.mapXtoCoord[x1]:
            if y1 != y2:

                curCount = 1
                sideLen = abs(y1 - y2)

                curCount = self.coordCount[x1+sideLen, y1] * self.coordCount[x1+sideLen, y2]

                curCount += self.coordCount[x1-sideLen, y1] * self.coordCount[x1-sideLen, y2]

                count += curCount

        return count

        
