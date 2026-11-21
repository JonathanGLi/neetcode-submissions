# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head.next == None:
            return 
        
        fast = head
        slow = head
        prev = slow

        while fast != None:
            fast = fast.next
            prev = slow
            slow = slow.next

            if not fast:
                break

            fast = fast.next
            if not fast:
                break
        print(slow.val)

        prev.next = None

        p = None
        c = None
        n = slow

        while n:
            p = c
            c = n
            n = n.next

            c.next = p


        l1 = head
        l2 = c

        cur = l1
        while cur:
            print(cur.val)
            cur = cur.next

        while l2.next:
            l1_n = l1.next
            l2_n = l2.next
            l1.next = l2
            l2.next = l1_n
            l1, l2 = l1_n, l2_n

        if l1.next:
            temp = l1.next
            l1.next = l2
            l2.next = temp
        else:
            l1.next = l2







