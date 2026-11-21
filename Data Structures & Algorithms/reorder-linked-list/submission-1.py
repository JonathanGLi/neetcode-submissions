# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #split link list in two

        slow = head
        fast = head.next

        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        slow.next = None




        #reverse second half
        prev = None
        cur = head2
        while(cur):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head2 = prev

        # print(head2.val)
        #zig zag and add all on final ll

        cur = head
        head = head.next
        while(head2 and head):
            cur.next = head2
            head2 = head2.next
            cur = cur.next

            cur.next = head
            head = head.next 
            cur = cur.next

        if head2:
            cur.next = head2
            head2 = head2.next
            cur = cur.next 

