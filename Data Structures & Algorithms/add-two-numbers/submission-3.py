# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()
        curNode = dummy

        ptr_1 = l1
        ptr_2 = l2

        carry = 0

        while ptr_1 or ptr_2:

            total = carry

            if ptr_1:
                total += ptr_1.val
                ptr_1 = ptr_1.next

            if ptr_2:
                total += ptr_2.val
                ptr_2 = ptr_2.next

            carry = 0
            if total >= 10:
                total -= 10
                carry = 1

            curNode.next = ListNode(val = total)
            curNode = curNode.next


        if carry == 1:
            curNode.next = ListNode(val = 1)

        return dummy.next








