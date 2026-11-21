"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:


    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #copy list into map
        m = {}
        m[None] = None

        cur = head

        while(cur):
            m[cur] = Node(cur.val)
            cur = cur.next

        #connect

        cur = head

        while(cur):
            if cur.next:
                m[cur].next = m[cur.next]
            else:
                m[cur].next = None
            if cur.random:
                m[cur].random = m[cur.random]
            else:
                m[cur].random = None
            cur = cur.next

        return m[head]


        
        