class Solution:
    def isHappy(self, n: int) -> bool:
        
        #R restate, done

        #Q questions
        # no negatives
        # can it end up noncyclic at any nunmber other than 1


        #E edge cases
        #0?


        #2 ways

        visited = set()

        #while loop
        while True:
            
            #compute sum with //10 % 10
            total = 0
            while n > 0:
                total += ((n%10)**2)
                n //= 10

            n = total

            print(n)

            #if total == 1 return True
            if n == 1:
                return True

            #if in visitedset return False
            elif n in visited:
                return False

            visited.add(n)


