# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        res = head

        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1

        print(n)

        start = head
        end = head
        a = None

        n -=1 

        while n > 0:

            for i in range(n):
                end = end.next

            #even case
            if start.next == end:
                end.next = None
                break
            a = start.next
            start.next = end
            end.next = a
            start = a
            end = a

            n -= 2
        if n == 0:
            start.next = None
        return None

        