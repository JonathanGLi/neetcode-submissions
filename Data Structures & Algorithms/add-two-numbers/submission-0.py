# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1 and not l2:
            return None
        elif l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2
        
        c1, c2 = l1, l2

        resHead = ListNode((c1.val + c2.val)%10)

        rem = ((c1.val + c2.val) >= 10)

        prev = resHead

        c1 = c1.next
        c2 = c2.next

        while (c1 or c2):
            
            if (c1 and c2):
                total = c1.val + c2.val
                if rem:
                    total+=1

                cur = ListNode(total%10)
                rem = (total >= 10)
                prev.next = cur
                prev = cur


                c1 = c1.next
                c2 = c2.next
            elif (c1):
                total = c1.val
                if rem:
                    total+=1

                cur = ListNode(total%10)
                rem = (total >= 10)
                prev.next = cur
                prev = cur

                c1 = c1.next
            elif (c2):
                total = c2.val
                if rem:
                    total+=1

                cur = ListNode(total%10)
                rem = (total >= 10)
                prev.next = cur
                prev = cur

                c2 = c2.next

        if rem:
            prev.next = ListNode(1)

        return resHead
