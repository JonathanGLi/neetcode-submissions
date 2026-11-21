# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None

        def mergerll(h1, h2):

            r = ListNode()
            i = r

            while h1 and h2:

                if h1.val < h2.val:
                    i.next = h1
                    i = i.next
                    h1 = h1.next
                else:
                    i.next = h2
                    i = i.next
                    h2 = h2.next

            if h1:
                i.next = h1
            else:
                i.next = h2
            return r.next

        while (len(lists) > 1):
            print(lists)
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(mergerll(l1, l2))
            lists = merged

            print(lists)

        print(lists)
        return lists[0]



