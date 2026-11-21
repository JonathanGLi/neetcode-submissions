class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        

        if len(hand) % groupSize != 0:
            return False

        hands = len(hand) // groupSize

        #create a dictionary mapping values to count
        counts = Counter(hand)

        # sort the hand 
        hand.sort()

        print(counts)

        print(hand)

        # iterate through sorted hand, 
        for i, card in enumerate(hand):

            print(card, counts)

            # if the count of the current val is > 0
            if counts[card] > 0:

                print(card, counts)

                # sub count to each number straight so if we get to 1, -1 count for 1, 2, 3, 4 if the groupSize is 4
                # if a count gets negqative, return False
                for j in range(groupSize):
                    if counts[card + j] <= 0:
                        return False
                    counts[card + j] -= 1

                print(card, counts)

                # if we have done this hands number of times return True
                hands -= 1

                if hands == 0:
                    return True

        return False

            