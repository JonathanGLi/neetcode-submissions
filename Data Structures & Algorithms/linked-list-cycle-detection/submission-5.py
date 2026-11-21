# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        fast = head
        slow = head
        if not fast:
            return False
        while True:
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            if not fast:
                break

            slow = slow.next

            if slow == fast:
                return True

        return False
            