# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()

        cur = dummy

        c1, c2 = l1, l2
        carry = 0

        while c1 or c2 or carry:

            c1v = c1.val if c1 else 0
            c2v = c2.val if c2 else 0

            summ = c1v + c2v + carry
            print(summ)

            carry = summ//10
            v = summ % 10

            cur.next = ListNode(val = v)
            cur = cur.next

            print(cur.val)

            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None

        return dummy.next 