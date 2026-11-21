# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        prev = ListNode()
        prev.next = head
        cur = head

        for i in range(n):
            cur = cur.next


        while (cur):
            cur = cur.next
            prev = prev.next

        if prev.next ==head:
            head = prev.next.next

        prev.next = prev.next.next

        return head