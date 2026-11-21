# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        i1 = list1
        i2 = list2
        res = ListNode()
        i3 = res

        while (i1!= None and i2 != None):
            if i1.val < i2.val:
                i3.next = i1
                i1 = i1.next
            else:
                i3.next = i2
                i2 = i2.next

            i3 = i3.next

        if i1 != None:
            i3.next = i1
        else:
            i3.next = i2

        return res.next
