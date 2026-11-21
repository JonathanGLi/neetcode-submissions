# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        
        slow = head
        fast = head

        while (True):

            fast = fast.next
            if fast == None:
                return False
            if fast == slow:
                return True

            fast = fast.next
            if fast == None:
                return False
            if fast == slow:
                return True


            slow = slow.next

            if fast == slow:
                return True