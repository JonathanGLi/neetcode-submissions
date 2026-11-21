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

        head1 = head
        while(head2):
            t2, t1 = head2.next, head1.next
            head1.next = head2
            head2.next = t1
            head1, head2 = t1, t2



